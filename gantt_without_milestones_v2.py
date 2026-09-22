# -*- coding: utf-8 -*-
"""
gantt_without_milestones_v2.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def create_gantt_without_milestones_v2():
    TASKS = [
        ("Επέκταση σώματος δεδομένων",              0.0, 1.5, "main"),
        ("Δυναμική επιλογή καρέ & χρονική προσοχή",  0.0, 2.0, "main"),
        ("Εξατομικευμένη προσαρμογή ανά ομιλητή",    1.0, 1.5, "main"),
        ("Μελέτη απομόνωσης γλωσσικής διόρθωσης",    1.5, 1.0, "sub"),
        ("Σύνθεση & εξατομίκευση φωνής",             2.0, 2.0, "main"),
        ("Διατερματικό σύστημα & φορητή εφαρμογή",   3.0, 1.0, "main"),
        ("Έγκριση ηθικής & δεοντολογίας",            0.5, 1.0, "sub"),
        ("Σταδιακή αποτίμηση στον πληθυσμό-στόχο",   1.5, 3.5, "main"),
        ("Συγγραφή διατριβής & υποστήριξη",          5.0, 1.0, "main"),
    ]

    SEMESTERS = [
        ("1ο εξάμηνο", ""),
        ("2ο εξάμηνο", ""),
        ("3ο εξάμηνο", ""),
        ("4ο εξάμηνο", ""),
        ("5ο εξάμηνο", ""),
        ("6ο εξάμηνο", ""),
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

    # --- διακεκομμένες γραμμές τριμήνων (μέση κάθε εξαμήνου) ---
    for i in range(N):
        ax.plot([i + 0.5, i + 0.5], [0, TOP], color=COLOR_GRID, lw=0.8, linestyle=(0, (3, 3)), zorder=1)

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
    ax.tick_params(axis="both", length=0, pad=8)

    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(False)
    ax.grid(False)

    ax.legend(handles=[Patch(facecolor=COLOR_MAIN, label="Κύριες εργασίες"),
                       Patch(facecolor=COLOR_SUB,  label="Υποστηρικτικές")],
              loc="lower right", bbox_to_anchor=(1.0, -0.14),
              frameon=False, fontsize=8.5, ncol=2)

    plt.tight_layout()
    fig.savefig("gantt_xoris_orosima_v2.svg", format="svg", bbox_inches="tight", facecolor="white")
    fig.savefig("gantt_xoris_orosima_v2.pdf", format="pdf", bbox_inches="tight", facecolor="white")
    fig.savefig("gantt_xoris_orosima_v2.png", format="png", dpi=300, bbox_inches="tight", facecolor="white")
    print("Έτοιμο: gantt_xoris_orosima_v2.svg, .pdf και .png")

if __name__ == "__main__":
    create_gantt_without_milestones_v2()