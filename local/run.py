from scenes.riemann_demo import RiemannDemo

if __name__ == "__main__":
    path = RiemannDemo().render_video()     # -> output_videos/RiemannDemo.mp4
    print("wrote", path)
