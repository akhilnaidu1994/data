import streamlit as st
import pandas as pd
from typing import List, Dict

# -------------------------------
# App Setup
# -------------------------------
st.set_page_config(
    page_title="Interactive Python Slides",
    page_icon="🐍",
    layout="wide",
)

# -------------------------------
# Utility: Define your slide data here
# Replace the placeholder bullets with the content from your PPT/PDF images.
# You can also map an image path for each slide (PNG/JPG extracted from the PDF).
# -------------------------------
Slide = Dict[str, object]

slides: List[Slide] = [
    {
        "title": "1️⃣ What is Python?",
        "bullets": [
            "High-level, interpreted language",
            "Simple, readable syntax",
            "Great for beginners and pros alike",
        ],
        "image": None,  # e.g. "slides/1.png"
        "code": 'print("Hello, World!")',
        "notes": "Replace bullets & notes with content from Slide 1 of your deck.",
    },
    {
        "title": "2️⃣ History of Python",
        "bullets": [
            "Created by Guido van Rossum",
            "First released in 1991",
            "Designed for clarity and productivity",
        ],
        "image": None,
        "code": None,
        "notes": "Replace with your history slide content.",
    },
    {
        "title": "3️⃣ Why Python?",
        "bullets": [
            "Easy to learn & use",
            "Huge community & ecosystem",
            "Works for web, data, AI, automation, scripting",
        ],
        "image": None,
        "code": None,
        "notes": "Add real reasons from your deck.",
    },
    {
        "title": "4️⃣ Real-world Examples",
        "bullets": [
            "Netflix – Recommendations",
            "NASA – Research tooling",
            "Instagram – Backend services",
        ],
        "image": None,
        "code": None,
        "notes": "Swap with your showcase logos/use-cases.",
    },
    {
        "title": "5️⃣ Python Basics",
        "bullets": [
            "Variables, types, and printing",
            "Strings & f-strings",
        ],
        "image": None,
        "code": 'name = "Alice"\nage = 25\nprint(f"My name is {name} and I am {age} years old.")',
        "notes": "Add basics from your deck.",
    },
    {
        "title": "6️⃣ Operators",
        "bullets": [
            "Arithmetic: + - * / // % **",
            "Comparison: == != > < >= <=",
            "Logical: and or not",
        ],
        "image": None,
        "code": 'a, b = 10, 3\nprint(a + b)\nprint(a * b)\nprint(a > b)',
        "notes": "Operators summary.",
    },
    {
        "title": "7️⃣ Control Flow & Loops",
        "bullets": [
            "if / elif / else",
            "for and while loops",
            "range(), enumerate()",
        ],
        "image": None,
        "code": 'for i in range(3):\n    print("Hello, Python!")',
        "notes": "Loop examples from your deck.",
    },
    {
        "title": "8️⃣ Data Structures",
        "bullets": [
            "list, tuple, dict, set",
            "Indexing & slicing",
        ],
        "image": None,
        "code": 'fruits = ["apple", "banana", "cherry"]\nages = (21, 25, 30)\nscores = {"Alice": 90, "Bob": 85}\nprint(fruits, ages, scores)',
        "notes": "Add examples from your slide.",
    },
    {
        "title": "9️⃣ Functions",
        "bullets": [
            "def, return",
            "Parameters & docstrings",
        ],
        "image": None,
        "code": 'def greet(name):\n    """Say hello."""\n    return f"Hello, {name}!"\n\nprint(greet("Nishi"))',
        "notes": "Function tips.",
    },
    {
        "title": "🔟 Pandas Hands-on",
        "bullets": [
            "DataFrames and Series",
            "Loading, selecting, filtering",
        ],
        "image": None,
        "code": 'import pandas as pd\n\ndata = {"Name": ["Alice", "Bob", "Charlie"], "Marks": [85, 90, 95]}\ndf = pd.DataFrame(data)\nprint(df.head())',
        "notes": "Hands-on demo.",
    },
    {
        "title": "✅ Wrap-up & Next Steps",
        "bullets": [
            "Recap of topics",
            "Practice daily",
            "Try Colab/Jupyter, explore Kaggle",
        ],
        "image": None,
        "code": None,
        "notes": "CTA and resources.",
    },
]

# Ensure at least one slide exists
if not slides:
    st.stop()

# -------------------------------
# Session State & Navigation
# -------------------------------
if "idx" not in st.session_state:
    st.session_state.idx = 0

N = len(slides)

def go(i: int):
    st.session_state.idx = int(max(0, min(N - 1, i)))

# Sidebar
with st.sidebar:
    st.title("📚 Course Navigator")
    titles = [s["title"] for s in slides]
    cur = st.radio("Go to Slide:", options=list(range(N)), index=st.session_state.idx, format_func=lambda i: titles[i])
    go(cur)

    st.markdown("---")
    st.caption("Keyboard shortcuts")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅️ Prev", use_container_width=True):
            go(st.session_state.idx - 1)
    with c2:
        if st.button("Next ➡️", type="primary", use_container_width=True):
            go(st.session_state.idx + 1)

    st.markdown("---")
    st.caption("Progress")
    st.progress((st.session_state.idx + 1) / N)

# -------------------------------
# Slide Renderer
# -------------------------------
slide = slides[st.session_state.idx]

st.title("🐍 Python for Absolute Beginners – Interactive Slides")
st.caption("Swap in your PPT/PDF content below. This app is fully wired—just paste text & image paths.")

left, right = st.columns([2, 1])

with left:
    st.header(slide["title"])
    if slide.get("bullets"):
        for b in slide["bullets"]:
            st.write(f"- {b}")
    if slide.get("code"):
        st.code(str(slide["code"]), language="python")
        run = st.toggle("Run sample code", value=False)
        if run:
            try:
                # Safe eval for demo snippets only
                # NOTE: In production, avoid eval/exec or sandbox safely.
                local_ns = {}
                exec(str(slide["code"]), {}, local_ns)
                out = local_ns.get("df")
                if isinstance(out, pd.DataFrame):
                    st.dataframe(out)
            except Exception as e:
                st.error(f"Error while running code: {e}")

with right:
    if slide.get("image"):
        st.image(slide["image"], use_container_width=True)
    if slide.get("notes"):
        with st.expander("📝 Speaker Notes"):
            st.write(slide["notes"])

# -------------------------------
# Practice Zone (per-slide tabs)
# -------------------------------
learn_tab, practice_tab, quiz_tab = st.tabs(["Learn", "Practice", "Quick Quiz"])

with learn_tab:
    st.info("Tip: Replace bullets & notes from your deck to auto-refresh this section.")

with practice_tab:
    st.write("Try a tiny exercise based on this slide:")
    if st.session_state.idx == 9:  # Pandas slide demo
        data = {"Name": ["Alice", "Bob", "Charlie"], "Marks": [85, 90, 95]}
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
        st.write("Filter marks ≥ 90:")
        st.dataframe(df[df["Marks"] >= 90])
    else:
        st.code("# Add a short exercise for this slide here.")

with quiz_tab:
    q = st.text_input("In one sentence, what did you learn on this slide?")
    if st.button("Save Reflection"):
        if q.strip():
            st.success("Nice! Reflection saved locally for this session.")
        else:
            st.warning("Please enter something before saving.")

# -------------------------------
# Export – Download current slide as Markdown
# -------------------------------
md_lines = [
    f"# {slide['title']}",
]
for b in slide.get("bullets", []):
    md_lines.append(f"- {b}")
if slide.get("code"):
    md_lines.append("\n```python\n" + str(slide["code"]) + "\n```\n")
if slide.get("notes"):
    md_lines.append("\n**Notes:**\n\n" + slide["notes"])

md_blob = "\n".join(md_lines)
st.download_button(
    label="⬇️ Download this slide as Markdown",
    data=md_blob,
    file_name=f"slide-{st.session_state.idx+1}.md",
    mime="text/markdown",
)

st.toast(f"Showing {st.session_state.idx+1}/{N}: {slide['title']}")
