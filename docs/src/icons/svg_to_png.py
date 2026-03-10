#!/usr/bin/env python3
"""
Convert SVG to PNG with custom resolution.
Requires: cairosvg library
Install with: pip install cairosvg
"""

import cairosvg
import argparse
from pathlib import Path


def svg_to_png(svg_path, output_path, width=None, height=None, dpi=96):
    """
    Convert SVG to PNG with specified resolution.
    
    Args:
        svg_path (str): Path to input SVG file
        output_path (str): Path to output PNG file
        width (int): Output width in pixels (maintains aspect ratio if height not specified)
        height (int): Output height in pixels (maintains aspect ratio if width not specified)
        dpi (int): DPI for rendering (default: 96)
    """
    try:
        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(output_path),
            output_width=width,
            dpi=dpi
        )
        print(f"✓ Successfully converted: {svg_path} -> {output_path}")
        print(f"  Resolution: {width or 'auto'} x {height or 'auto'} pixels")
    except Exception as e:
        print(f"✗ Error converting {svg_path}: {e}")

def svg_to_pdf(svg_path, output_path, width=None, height=None, dpi=96):
    """
    Convert SVG to PDF with specified resolution.
    
    Args:
        svg_path (str): Path to input SVG file
        output_path (str): Path to output PDF file
        width (int): Output width in pixels (maintains aspect ratio if height not specified)
        height (int): Output height in pixels (maintains aspect ratio if width not specified)
        dpi (int): DPI for rendering (default: 96)
    """
    try:
        cairosvg.svg2pdf(
            url=str(svg_path),
            write_to=str(output_path),
            output_width=width,
            dpi=dpi
        )
        print(f"✓ Successfully converted: {svg_path} -> {output_path}")
        print(f"  Resolution: {width or 'auto'} x {height or 'auto'} pixels")
    except Exception as e:
        print(f"✗ Error converting {svg_path}: {e}")


if __name__ == "__main__":    
    svg_path = './iadl_logo.svg'
    output_path = './iadl_logo.png'
    width = 480
    height = 60
    dpi = 300

    svg_to_png(svg_path, output_path, width, dpi)
    svg_to_pdf(svg_path, './iadl_logo.pdf', width, dpi)