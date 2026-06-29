"""
Convert PDF maps to JPG images for the portfolio
Run this script to convert map 2.pdf, map 3.pdf, and map 4.pdf to JPG format
"""

try:
    from pdf2image import convert_from_path
    import os

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the PDF files to convert
    pdf_files = ['map 2.pdf', 'map 3.pdf', 'map 4.pdf']
    output_names = ['toronto-map-1.jpg', 'toronto-map-2.jpg', 'toronto-map-3.jpg']

    for pdf_file, output_name in zip(pdf_files, output_names):
        pdf_path = os.path.join(script_dir, pdf_file)
        output_path = os.path.join(script_dir, output_name)

        if os.path.exists(pdf_path):
            print(f"Converting {pdf_file}...")
            # Convert PDF to images
            images = convert_from_path(pdf_path, dpi=150)

            # Save the first page as JPG
            if images:
                images[0].save(output_path, 'JPEG', quality=85)
                print(f"✓ Saved as {output_name}")
        else:
            print(f"✗ File not found: {pdf_file}")

    print("\n✓ Conversion complete!")
    print("\nGenerated files:")
    for name in output_names:
        if os.path.exists(os.path.join(script_dir, name)):
            print(f"  - {name}")

except ImportError:
    print("Error: pdf2image library not installed")
    print("\nTo install, run:")
    print("  pip install pdf2image")
    print("  pip install pillow")
    print("\nYou may also need to install poppler:")
    print("  Windows: Download from https://github.com/oschwartz10612/poppler-windows/releases/")
    print("  Add poppler/bin to your PATH")
except Exception as e:
    print(f"Error: {e}")
    print("\nAlternative method:")
    print("1. Open each PDF file (map 2.pdf, map 3.pdf, map 4.pdf)")
    print("2. Take a screenshot or export as image")
    print("3. Save as:")
    print("   - map 2.pdf → toronto-map-1.jpg")
    print("   - map 3.pdf → toronto-map-2.jpg")
    print("   - map 4.pdf → toronto-map-3.jpg")