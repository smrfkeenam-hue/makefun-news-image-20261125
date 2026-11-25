import os

# Copy the pre-drawn news image of 25 November 2026 to the output dir.
# The image is a newspaper front page: six real stories of the day,
# drawn with PIL and stored as entry.png in this repository.
src = os.path.join(os.path.dirname(__file__), "entry.png")
dst_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(dst_dir, exist_ok=True)
with open(src, "rb") as f:
    data = f.read()
with open(os.path.join(dst_dir, "entry.png"), "wb") as f:
    f.write(data)
print("entry.png written:", len(data), "bytes")
