import subprocess
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = Path(__file__).parent
IGNORED = {"_build", "__pycache__", ".ipynb_checkpoints", ".git"}


def git(*args):
    result = subprocess.run(
        ["git", "-C", str(WATCH_DIR), *args],
        capture_output=True, text=True
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def push_to_github(path: str, action: str):
    rel = Path(path).relative_to(WATCH_DIR)

    if rel.suffix != ".ipynb":
        return
    if any(part in IGNORED for part in rel.parts):
        return

    print(f"\n📁 {action}: {rel}")

    code, out, err = git("add", str(path))
    if code != 0:
        print(f"  git add failed: {err}")
        return

    code, diff, _ = git("diff", "--cached", "--name-only")
    if not diff:
        print("  Nothing new to commit.")
        return

    msg = f"{action}: {rel}"
    code, out, err = git("commit", "-m", msg)
    if code != 0:
        print(f"  git commit failed: {err}")
        return
    print(f"  ✅ Committed: {msg}")

    code, out, err = git("push", "-u", "origin", "HEAD")
    if code != 0:
        print(f"  ❌ Push failed: {err}")
    else:
        print(f"  🚀 Pushed to GitHub")


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            push_to_github(event.src_path, "Add notebook")


if __name__ == "__main__":
    print(f"👀 Watching: {WATCH_DIR}")
    print("   Any new .ipynb notebook added will be pushed to GitHub automatically.")
    print("   Press Ctrl+C to stop.\n")

    observer = Observer()
    observer.schedule(Handler(), str(WATCH_DIR), recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nWatcher stopped.")
    observer.join()
