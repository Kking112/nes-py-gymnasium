# Gymnasium Migration Guide

This project migrated from the legacy OpenAI Gym API to Gymnasium.

Key API changes for users:
- Imports: use `import gymnasium as gym` and `from gymnasium import spaces`.
- `reset` now returns `(observation, info)` instead of only `observation`.
- `step` now returns a 5-tuple `(observation, reward, terminated, truncated, info)`.
  - `terminated` replaces the old `done` for terminal states.
  - `truncated` indicates time limits or external truncation (false by default here).
- Rendering: set `render_mode` in the environment constructor. Call `env.render()` without a mode.
  - Supported: `render_mode="rgb_array"` (returns ndarray), `render_mode="human"` (displays window).
- Seeding: prefer `env.reset(seed=...)`; `env.seed()` remains for compatibility and warns.

Python and dependencies:
- Supported Python versions: 3.11–3.13 (3.14 experimental initially).
- Dependencies: `gymnasium>=0.29`, `numpy>=1.26`, `pyglet>=2.0`, `tqdm>=4.64`.

Notes for developers:
- NESEnv implements Gymnasium’s signatures and metadata (`render_modes`, `render_fps`).
- Wrappers (e.g., JoypadSpace) propagate Gymnasium return shapes.
- Tests updated to reflect new return conventions and rendering pattern.
