import pandas as pd
from pathlib import Path

df = pd.read_csv("_annotations.csv")
classes = ["License_Plate"]  # sınıf isimlerini burada belirt

(Path("labels")).mkdir(exist_ok=True)

for img, grp in df.groupby("filename"):
    w = int(grp["width"].iloc[0])
    h = int(grp["height"].iloc[0])
    lines = []
    for _, r in grp.iterrows():
        cls_id = classes.index(r["class"])
        x_c = ((r["xmin"] + r["xmax"]) / 2) / w
        y_c = ((r["ymin"] + r["ymax"]) / 2) / h
        bw = (r["xmax"] - r["xmin"]) / w
        bh = (r["ymax"] - r["ymin"]) / h
        lines.append(f"{cls_id} {x_c:.6f} {y_c:.6f} {bw:.6f} {bh:.6f}")
    Path("labels")/f"{Path(img).stem}.txt"
    with open(Path("labels")/f"{Path(img).stem}.txt", "w") as f:
        f.write("\n".join(lines))
