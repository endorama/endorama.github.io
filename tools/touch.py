#!/usr/bin/env python
import frontmatter
import sys
from datetime import datetime, timezone

if __name__ == "__main__":
    original = ""
    post = ""
    with open(sys.argv[1], "r") as f:
        post = frontmatter.load(f)
        original = post

    # 2022-08-16T23:34:07+02:00
    post["date"] = datetime.now(timezone.utc).astimezone().isoformat('T', 'seconds')

    with open(sys.argv[1], "w") as f:
        try:
            f.write(frontmatter.dumps(post, sort_keys=False))
        except:
            f.write(original)