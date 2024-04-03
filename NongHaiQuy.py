# Nông Hải Quý
# Đề bài: Đọc 1 file văn bản gồm nhiều dòng. GHi ra màn hình theo thứ tự ngược lại của các dòng
# Bài làm
# Kiểm tra đuôi tệp
def check_file_extension(filename):
    allowed_extensions = ['.txt']

    if not any(filename.endswith(ext) for ext in allowed_extensions):
        return False
    return True

# Nhập tên tệp từ người dùng
filename = input("Nhập tên tệp: ")

# Kiểm tra đuôi tệp
if not check_file_extension(filename):
    print("Lỗi file: Đuôi tệp không hợp lệ.")
else:
    try:
        # Mở file văn bản để đọc
        with open(filename, 'r', encoding='utf-8') as file:
            # Đọc từng dòng trong file và lưu vào list
            lines = file.readlines()

            # In các dòng theo thứ tự ngược lại
            for line in reversed(lines):
                print(line.strip())

    except FileNotFoundError:
        print("Không tồn tại tệp.")
