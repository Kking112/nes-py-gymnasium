#!/usr/bin/env python3
"""Demo script to run random actions in the NES environment with real-time rendering.

Usage:
  uv run demo.py --rom path/to/rom.nes [--steps 0] [--seed 0]

Notes:
- Requires a valid NES ROM file path.
- Uses Gymnasium-style API (reset -> (obs, info), step -> 5-tuple).
"""
import argparse
import time
from nes_py.nes_env import NESEnv


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rom", "-r", required=True, type=str, help="Path to NES ROM (.nes)")
    parser.add_argument("--steps", "-s", type=int, default=0, help="Number of steps to run (0 = run forever)")
    parser.add_argument("--seed", type=int, default=None, help="Optional seed for env.reset")
    args = parser.parse_args()

    env = NESEnv(args.rom, render_mode="human")
    steps = args.steps

    try:
        _, _ = env.reset(seed=args.seed)
        fps = env.metadata.get("render_fps", env.metadata.get("video.frames_per_second", 60))
        target_dt = 1.0 / float(fps) if fps else 0.0
        i = 0
        while steps <= 0 or i < steps:
            i += 1
            action = env.action_space.sample()
            _, _, terminated, truncated, _ = env.step(action)
            env.render()
            if terminated or truncated:
                _, _ = env.reset()
            if target_dt > 0:
                time.sleep(target_dt)
    except KeyboardInterrupt:
        pass
    finally:
        env.close()


if __name__ == "__main__":
    main()
