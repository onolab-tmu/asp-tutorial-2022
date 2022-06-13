"""Make progress chart of onolab members."""
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def get_progress():
    cwd = Path(".")
    data = {
        "user": [],
        "chapter": [],
        "progress": [],
    }
    users = list(
        filter(lambda x: x.is_dir() and x.name not in IGNORE, sorted(cwd.iterdir()))
    )

    # user ごとの progress を取得する
    for user in users:
        for chap, max_cnt in zip(range(n_chapters), n_codes):
            # user/chapterXX の path (章だけ 1-indexed なので num+1)
            chapter_path = Path(user / f"chapter{chap+1:02d}")

            # user/chapterXX に含まれる .py ファイルをカウント
            py_files = list(chapter_path.glob("[0-9][0-9].py"))

            # 問題数は max_cnt が上限で、それ以上のファイル数が含まれる場合は max_cnt にする
            n_solved = min(len(py_files), max_cnt)

            data["user"] += [user]
            data["chapter"] += [chap + 1]
            data["progress"] += [n_solved / max_cnt]

    return data


def plot_progress(data):
    df = pd.DataFrame(data)

    sns.set(style="white", context="notebook")
    sns.set_palette("hls", n_chapters)

    g = sns.catplot(
        data=df,
        y="user",
        x="progress",
        hue="chapter",
        kind="bar",
        aspect=1.5,
    )
    g.set(xlim=(0, 1))
    g.despine(top=False, right=False)

    plt.subplots_adjust(bottom=0.10)
    plt.savefig("progress.png")


def main():
    data = get_progress()
    if len(list(data.keys())):
        plot_progress(data)


if __name__ == "__main__":
    # 章数と各章の問題数
    n_chapters, n_codes = 10, [10 for _ in range(10)]

    # progress bar に表示しないディレクトリ名
    IGNORE = [".git", ".github", ".automation"]

    main()
