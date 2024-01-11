import click
import PyPDF2


def split(page, width, height, left_margin, right_margin, top_margin, bottom_margin):
    page.mediabox.lower_left = (left_margin, bottom_margin)
    page.mediabox.lower_right = (width - right_margin, bottom_margin)
    page.mediabox.upper_left = (left_margin, height - top_margin)
    page.mediabox.upper_right = (width - right_margin, height - top_margin)


@click.command()
@click.option("-i", help="pdf文件路径")
@click.option("-o", help="输出pdf文件路径")
@click.option("-l", default=90, help="左边去除宽度")
@click.option("-r", default=80, help="右边去除宽度")
@click.option("-t", default=70, help="上边去除高度")
@click.option("-b", default=70, help="下边去除高度")
def main(i, o, l, r, t, b):
    """裁剪生成新的PDF."""
    left_margin = int(l)
    right_margin = int(r)
    top_margin = int(t)
    bottom_margin = int(b)
    input_file_path = i
    input_file = PyPDF2.PdfReader(open(input_file_path, "rb"))
    output_file = PyPDF2.PdfWriter()
    page_info = input_file.pages[0]  # 以第一页为标准获得宽度和高度
    width = float(page_info.mediabox.width)  # 宽度
    height = float(page_info.mediabox.height)  # 高度
    print(f"pdf原有的宽:{width},高:{height}")
    page_count = len(input_file.pages)  # 统计页数
    for page_num in range(page_count):
        this_page = input_file.pages[page_num]
        split(
            this_page,
            width,
            height,
            left_margin,
            right_margin,
            top_margin,
            bottom_margin,
        )
        output_file.add_page(this_page)
        output_file.write(open(o, "wb"))


if __name__ == "__main__":
    main()
