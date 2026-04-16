# Essentials of Embodied AI Research

[![Documentation Status](https://readthedocs.org/projects/essentials-of-eai-research/badge/?version=latest)](https://essentials-of-eai-research.readthedocs.io/en/latest/?badge=latest)

A comprehensive, incrementally-updated learning resource for PhD students, covering:

- **Reinforcement Learning** — from fundamentals to advanced algorithms
- **World Models** — representation learning, video prediction, and planning
- **Embodied AI** — locomotion, loco-manipulation, teleoperation, and data collection
- **Distributed RL** — architecture paradigms, frameworks, and scaling

Inspired by [Spinning Up in Deep RL](https://spinningup.openai.com/), this resource provides structured, in-depth material with bilingual (English/Chinese) support.

## Quick Start

### Read Online

Visit the documentation at: **[essentials-of-eai-research.readthedocs.io](https://essentials-of-eai-research.readthedocs.io/)**

Use the language switcher in the top navigation to toggle between English and 中文.

### Build Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally with hot-reload
mkdocs serve

# Build static site
mkdocs build
```

The site will be available at `http://127.0.0.1:8000/`.

## Project Structure

```
essentials-of-eai-research/
├── mkdocs.yml              # MkDocs configuration
├── .readthedocs.yaml       # ReadTheDocs build config
├── requirements.txt        # Python dependencies
└── docs/
    ├── en/                 # English content
    │   ├── index.md
    │   ├── introduction.md
    │   ├── rl/             # Reinforcement Learning
    │   ├── world_models/   # World Models
    │   ├── embodied/       # Embodied AI
    │   ├── distributed_rl/ # Distributed RL
    │   └── resources/      # Exercises, reading lists
    ├── zh/                 # Chinese content (中文内容)
    │   └── ...             # Mirror structure
    ├── stylesheets/        # Custom CSS
    ├── javascripts/        # MathJax config
    └── assets/             # Images and diagrams
```

## Contributing

We welcome contributions! To add or improve content:

1. Fork the repository
2. Create a feature branch
3. Write content in both `docs/en/` and `docs/zh/` (or just one language)
4. Submit a pull request

### Content Guidelines

- Use clear, accessible language suitable for early-stage PhD students
- Include mathematical formulations with LaTeX (`$...$` for inline, `$$...$$` for display)
- Cite seminal papers with links to arXiv or project pages
- Add diagrams and figures in `docs/assets/img/`
- Mark incomplete sections with `!!! warning "Work in Progress"` admonitions

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
