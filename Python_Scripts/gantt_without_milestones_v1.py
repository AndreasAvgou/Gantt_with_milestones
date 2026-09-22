# -*- coding: utf-8 -*-
"""
gantt_without_milestones_v1.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def create_gantt_without_milestones_v1():
    TASKS = [
        ("Επέκταση σώματος δεδομένων",              0.0, 1.5, "main"),
        ("Δυναμική επιλογή καρέ",                    0.0, 2.0, "main"),
        ("Εξατομικευμένη προσαρμογή ανά ομιλητή",    1.0, 1.5, "main"),
        ("Σύνθεση & εξατομίκευση φωνής",             2.0, 2.0, "main"),
        ("Διατερματικό σύστημα & φορητή εφαρμογή",   3.0, 1.0, "main"),
        ("Αποτίμηση στον πληθυσμό-στόχο",            4.0, 1.2, "main"),
        ("Συγγραφή διατριβής & υποστήριξη",          5.0, 1.0, "main"),
    ]

    SEMESTERS = [
        ("1ο εξάμηνο", "10/26 – 03/27"),
        ("2ο εξάμηνο", "04/27 – 09/27"),
        ("3ο εξάμηνο", "10/27 – 03/28"),
        ("4ο εξάμηνο", "04/28 – 09/28"),
        ("5ο εξάμηνο", "10/28 – 03/29"),
        ("6ο εξάμηνο", "04/29 – 09/29"),
    ]

    COLOR_MAIN = "#3A5A73"
    COLOR_SUB  = "#7A98AE"
    COLOR_GRID = "#D0D5D9"
    COLOR_BAND = "#F4F6F7"
    COLOR_TEXT = "#1A1A1A"
    COLOR_MUTE = "#5A6570"

    plt.rcParams["font.family"] = ["DejaVu Sans"]

    N = len(SEMESTERS)
    fig, ax = plt.subplots(figsize=(13, 5.6), dpi=150)
    TOP = len(TASKS)

    for i in range(N):
        if i % 2 == 1:
            ax.add_patch(plt.Rectangle((i, 0), 1, TOP, color=COLOR_BAND, linewidth=0, zorder=0))

    for i in range(N + 1):
        ax.plot([i, i], [0, TOP], color=COLOR_GRID, lw=1, zorder=1)

    ax.plot([0, N], [0, 0], color="#9AA3AA", lw=1.2, zorder=2)

    for row, (label, start, span, kind) in enumerate(TASKS):
        y = len(TASKS) - row - 1
        color = COLOR_MAIN if kind == "main" else COLOR_SUB
        ax.broken_barh([(start, span)], (y + 0.25, 0.5), facecolors=color, edgecolor="none", zorder=3)

    ax.set_yticks([len(TASKS) - i - 1 + 0.5 for i in range(len(TASKS))])
    ax.set_yticklabels([t[0] for t in TASKS], fontsize=10.5, color=COLOR_TEXT)
    ax.set_ylim(-0.35, len(TASKS))
    ax.set_xlim(0, N)

    ax.xaxis.set_ticks_position("top")
    ax.set_xticks([i + 0.5 for i in range(N)])
    ax.set_xticklabels([s[0] for s in SEMESTERS], fontsize=10.5, fontweight="bold", color=COLOR_TEXT)
    ax.tick_params(axis="both", length=0, pad=22)

    for i, (_, period) in enumerate(SEMESTERS):
        ax.annotate(period, xy=(i + 0.5, 1.0), xycoords=("data", "axes fraction"),
                    xytext=(0, 7), textcoords="offset points",
                    ha="center", va="bottom", fontsize=8.5,
                    color=COLOR_MUTE, annotation_clip=False)

    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(False)
    ax.grid(False)

    ax.legend(handles=[Patch(facecolor=COLOR_MAIN, label="Κύριες εργασίες")],
              loc="lower right", bbox_to_anchor=(1.0, -0.14),
              frameon=False, fontsize=8.5, ncol=2)

    plt.tight_layout()
    fig.savefig("gantt_xoris_orosima_v1.svg", format="svg", bbox_inches="tight", facecolor="white")
    fig.savefig("gantt_xoris_orosima_v1.pdf", format="pdf", dpi=300, bbox_inches="tight", facecolor="white")
    print("Έτοιμο: gantt_xoris_orosima_v1.svg και .pdf")

if __name__ == "__main__":
    create_gantt_without_milestones_v1()