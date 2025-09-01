import base64
import sys
from PIL import Image, ImageDraw, ImageFont

def convert_from_kryptor(filename):
	with open(filename, 'r') as file:
		b64_str = file.read(48)
	decoded = base64.b64decode(b64_str)
	hex_str = decoded.hex()
	# Split hex encoded public key into separate hexidecimal colors
	color_chunks = [hex_str[i:i+6] for i in range(0, len(hex_str)-4, 6)]
	# cut excess four characters to be used as text in bottom right
	last = hex_str[-4:]
	last_chunks = [last[:2], last[2:]]
	print(' '.join([chunk.upper() for chunk in color_chunks + last_chunks]))

	# Create flag image with vertical stripes
	create_flag_image(color_chunks, last_chunks)

def create_flag_image(color_chunks, last_chunks, filename='flag.png', width=1100, height=550):
	stripe_width = width // len(color_chunks)
	img = Image.new('RGB', (width, height))
	for i, chunk in enumerate(color_chunks):
		chunk = chunk.ljust(6, '0')
		rgb = tuple(int(chunk[j:j+2], 16) for j in (0, 2, 4))
		for x in range(i*stripe_width, (i+1)*stripe_width):
			for y in range(height):
				img.putpixel((x, y), rgb)
	# Add text with bottom right
	draw = ImageDraw.Draw(img)
	text = f"+ {last_chunks[0].upper()} {last_chunks[1].upper()}"
	font = ImageFont.truetype("arial.ttf", 64)
	bbox = draw.textbbox((0, 0), text, font=font)
	text_width = bbox[2] - bbox[0]
	text_height = bbox[3] - bbox[1]
	x = img.width - text_width - 20
	y = img.height - text_height - 20
	draw.text((x, y), text, fill=(255,255,255), font=font)
	img.save(filename)
	print(f'Flag image saved as {filename}')

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python marcottegen.py <Kryptor public key file>")
	else:
		convert_from_kryptor(sys.argv[1])

