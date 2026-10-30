import html
from datetime import date, datetime, timedelta
from uuid import uuid4

import streamlit as st


st.set_page_config(page_title="Little Life Log", page_icon="🌿", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap');

    :root {
        --paper: #f6f5ee;
        --ink: #202a23;
        --muted: #747b70;
        --line: #dedfd4;
        --green: #355d43;
        --lime: #d7ed9b;
        --coral: #e47d61;
        --white: #fffefa;
    }

    .stApp { background: var(--paper); color: var(--ink); }
    .block-container { max-width: 1120px; padding-top: 2rem; padding-bottom: 4rem; }
    h1, h2, h3, [data-testid="stMarkdownContainer"] p, label, button {
        font-family: "DM Sans", sans-serif;
    }
    h1, h2, h3 { color: var(--ink); }
    .masthead {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid var(--line);
        padding: 0 0 18px;
        color: var(--ink);
        font: 700 13px "DM Sans", sans-serif;
        letter-spacing: .02em;
    }
    .brand-mark {
        display: inline-grid;
        width: 30px;
        height: 30px;
        place-items: center;
        margin-right: 8px;
        border-radius: 50%;
        background: var(--lime);
        color: var(--green);
        font-size: 17px;
    }
    .today-label, .eyebrow {
        color: var(--muted);
        font: 700 11px "DM Sans", sans-serif;
        letter-spacing: .1em;
        text-transform: uppercase;
    }
    .hero-title {
        margin: 14px 0 16px;
        color: var(--ink);
        font: 500 clamp(42px, 6vw, 70px)/.98 "Fraunces", Georgia, serif;
    }
    .hero-title span { color: var(--green); }
    .hero-copy {
        max-width: 420px;
        color: var(--muted);
        font: 400 15px/1.7 "DM Sans", sans-serif;
    }
    .count-line {
        margin-top: 22px;
        color: var(--green);
        font: 700 12px "DM Sans", sans-serif;
    }
    .count-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        margin-right: 8px;
        border-radius: 50%;
        background: var(--coral);
    }
    .cover-note {
        position: relative;
        display: inline-block;
        margin: -58px 0 26px 18px;
        padding: 10px 13px;
        background: var(--white);
        color: var(--ink);
        font: 600 11px "DM Sans", sans-serif;
        transform: rotate(-2deg);
    }
    .section-rule { border-top: 1px solid var(--line); margin: 18px 0 26px; }
    .moment {
        display: grid;
        grid-template-columns: 76px minmax(0, 1fr) auto;
        gap: 16px;
        align-items: start;
        padding: 20px 0;
        border-bottom: 1px solid var(--line);
    }
    .moment-date { padding-top: 3px; color: var(--muted); font: 400 12px/1.5 "DM Sans", sans-serif; }
    .moment-mood { margin-bottom: 8px; color: var(--green); font: 700 11px "DM Sans", sans-serif; }
    .moment-mood::before {
        display: inline-block;
        width: 7px;
        height: 7px;
        margin-right: 7px;
        border-radius: 50%;
        background: var(--coral);
        content: "";
    }
    .moment-note { color: var(--ink); font: 400 14px/1.65 "DM Sans", sans-serif; overflow-wrap: anywhere; }
    div[data-testid="stForm"] {
        padding: 21px;
        border: 1px solid var(--line);
        border-radius: 4px;
        background: var(--white);
    }
    div[data-testid="stForm"] h3 { font: 500 25px "Fraunces", Georgia, serif; }
    div[data-testid="stForm"] label { color: var(--muted); font-size: 12px; }
    .stTextArea textarea, .stDateInput input {
        border-color: var(--line);
        border-radius: 3px;
        background: #fff;
        color: var(--ink);
    }
    .stButton > button, .stFormSubmitButton > button {
        border: 0;
        border-radius: 3px;
        background: var(--green);
        color: #fff;
        font-weight: 700;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover {
        border: 0;
        background: #294b35;
        color: #fff;
    }
    @media (max-width: 700px) {
        .block-container { padding: 1.25rem 1rem 3rem; }
        .moment { grid-template-columns: 58px minmax(0, 1fr); gap: 10px; }
        .moment .remove-slot { grid-column: 2; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def make_starter_entries(today: date) -> list[dict[str, str]]:
    return [
        {
            "id": "sample-1",
            "date": (today - timedelta(days=1)).isoformat(),
            "mood": "Calm",
            "note": "Made tea after work and called Mum. We talked about absolutely nothing, which was exactly what I needed.",
        },
        {
            "id": "sample-2",
            "date": (today - timedelta(days=2)).isoformat(),
            "mood": "Good",
            "note": "Found a little bookshop on the walk home. Bought a poetry collection and took the scenic route.",
        },
        {
            "id": "sample-3",
            "date": (today - timedelta(days=3)).isoformat(),
            "mood": "Tired",
            "note": "A long day, but dinner with Sam made it feel smaller. Remember to make plans just because.",
        },
    ]


today = date.today()
if "entries" not in st.session_state:
    st.session_state.entries = make_starter_entries(today)

st.markdown(
    f'<div class="masthead"><span><span class="brand-mark">*</span>LITTLE LIFE LOG</span>'
    f'<span class="today-label">{today.strftime("%A, %B %-d")}</span></div>',
    unsafe_allow_html=True,
)

hero, cover = st.columns([1.05, 0.95], gap="large", vertical_alignment="center")
with hero:
    st.markdown('<div class="eyebrow">A small record of being here</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-title">Life, lately.<br><span>One day at a time.</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-copy">The ordinary bits count, too. Keep a note of what happened, '
        'how it felt, and what you want to remember.</div>',
        unsafe_allow_html=True,
    )
    entry_count = len(st.session_state.entries)
    st.markdown(
        f'<div class="count-line"><span class="count-dot"></span>{entry_count} '
        f'{"moment" if entry_count == 1 else "moments"} collected</div>',
        unsafe_allow_html=True,
    )

with cover:
    st.image(
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1200&q=85",
        width="stretch",
        output_format="auto",
    )
    st.markdown('<div class="cover-note">take the long way home</div>', unsafe_allow_html=True)

st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
log_column, form_column = st.columns([1.8, 1], gap="large")

with log_column:
    st.markdown('<div class="eyebrow">The recent pages</div>', unsafe_allow_html=True)
    st.subheader("Little moments")
    sorted_entries = sorted(st.session_state.entries, key=lambda entry: entry["date"], reverse=True)
    if not sorted_entries:
        st.caption("No moments written down yet. Start with one small thing from today.")

    for entry in sorted_entries:
        moment_date = datetime.fromisoformat(entry["date"]).strftime("%b %-d")
        date_column, note_column, remove_column = st.columns([0.19, 0.68, 0.13], gap="small")
        with date_column:
            st.markdown(f'<div class="moment-date">{moment_date}</div>', unsafe_allow_html=True)
        with note_column:
            safe_mood = html.escape(entry["mood"])
            safe_note = html.escape(entry["note"])
            st.markdown(f'<div class="moment-mood">{safe_mood}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="moment-note">{safe_note}</div>', unsafe_allow_html=True)
        with remove_column:
            if st.button("Remove", key=f"remove-{entry['id']}"):
                st.session_state.entries = [
                    item for item in st.session_state.entries if item["id"] != entry["id"]
                ]
                st.rerun()
        st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)

with form_column:
    st.markdown('<div class="eyebrow">Make a note</div>', unsafe_allow_html=True)
    st.markdown("### What was today like?")
    with st.form("entry-form", clear_on_submit=True):
        mood = st.radio("Pick a feeling", ["Good", "Calm", "Tired", "Full"], horizontal=True)
        entry_date = st.date_input("Date", value=today)
        note = st.text_area(
            "A moment worth keeping",
            max_chars=500,
            placeholder="A good conversation, a tiny win, something you noticed...",
        )
        submitted = st.form_submit_button("Save this moment", width="stretch")

    if submitted:
        if not note.strip():
            st.warning("Write a few words before saving your moment.")
        else:
            st.session_state.entries.append(
                {
                    "id": uuid4().hex,
                    "date": entry_date.isoformat(),
                    "mood": mood,
                    "note": note.strip(),
                }
            )
            st.rerun()

st.caption("Entries are kept in this browser session. They are cleared when the session ends.")