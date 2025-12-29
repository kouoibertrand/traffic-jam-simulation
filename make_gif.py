import imageio
import glob

frames = sorted(glob.glob("frame_*.png"))
images = [imageio.imread(f) for f in frames]
imageio.mimsave("traffic.gif", images, duration=0.1)  # 0.1s par frame