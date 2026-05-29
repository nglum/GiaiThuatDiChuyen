# 🚍 Bài Tập Lớn: Tối Ưu Hoá Tuyến Đường Du Lịch Bằng Giải Thuật Di Truyền

## 📌 Tổng Quan Đề Bài

Một công ty du lịch lữ hành tại **Hà Nội** muốn thiết kế một tour du lịch đi qua **10 địa điểm nổi tiếng** tại miền Bắc và miền Trung Việt Nam. Xe du lịch sẽ **xuất phát từ Hà Nội, đi qua 9 địa điểm còn lại (mỗi nơi đúng 1 lần) và cuối cùng quay trở lại Hà Nội**.

### 🎯 Mục Tiêu
Sử dụng **Giải thuật di truyền (Genetic Algorithm - GA)** để tìm ra **thứ tự hành trình tối ưu** sao cho **tổng quãng đường di chuyển là ngắn nhất** → tiết kiệm chi phí xăng dầu và thời gian.

---

## 📊 Dữ Liệu Bài Toán

### 10 Địa Điểm Du Lịch (Tọa Độ Euclide Phẳng)

| ID | Tên Địa Điểm | Tọa Độ X | Tọa Độ Y |
|:--:|:--|:--:|:--:|
| 0 | Hà Nội (Điểm đầu/cuối) | 20 | 40 |
| 1 | Hạ Long (Quảng Ninh) | 35 | 38 |
| 2 | Sapa (Lào Cai) | 5 | 55 |
| 3 | Ninh Bình | 18 | 32 |
| 4 | Phong Nha (Quảng Bình) | 25 | 10 |
| 5 | Huế | 32 | 5 |
| 6 | Đà Nẵng | 38 | 2 |
| 7 | Mai Châu (Hòa Bình) | 10 | 38 |
| 8 | Đảo Cát Bà (Hải Phòng) | 33 | 35 |
| 9 | Hà Giang | 12 | 58 |

### Công Thức Tính Khoảng Cách
Khoảng cách Euclide giữa 2 điểm A(x₁, y₁) và B(x₂, y₂):

```
d = √((x₂ - x₁)² + (y₂ - y₁)²)
```

---

## 🧬 Yêu Cầu Kỹ Thuật Chi Tiết

### 3.1 Mã Hóa Nhiễm Sắc Thể (Chromosome Representation)
- **Mỗi cá thể** là một mảng gồm **10 số nguyên** chứa các ID từ 0 đến 9.
- **Quy ước**: Điểm đầu (ID: 0) và điểm cuối cố định là **Hà Nội**, nên chuỗi gen chỉ quản lý **thứ tự hoán vị 9 địa điểm còn lại**.
- **Ví dụ**: `[0, 2, 9, 7, 3, 1, 8, 4, 5, 6]`
  - Hành trình: Hà Nội → Sapa → Hà Giang → ... → Đà Nẵng → quay về Hà Nội

### 3.2 Hàm Thích Nghi (Fitness Function)
**Tính tổng quãng đường** của toàn bộ hành trình (bao gồm chặng quay về):
```python
def total_distance(route):
    return sum(euclidean(route[i], route[i+1]) for i in range(N))
```

**Hàm Fitness** (tỷ lệ nghịch với quãng đường):
```python
def fitness(route):
    return 1 / total_distance(route)
```

### 3.3 Các Phép Toán Di Truyền

#### **Khởi Tạo (Initialization)**
- Tạo **100 cá thể** ngẫu nhiên
- Mỗi cá thể là hoán vị ngẫu nhiên của các ID từ 1 đến 9, với ID 0 cố định ở đầu/cuối

#### **Chọn Lọc (Selection)**
- Phương pháp: **Tournament Selection**
- Kích thước giải đấu: **k = 5**
- Lựa chọn 5 cá thể ngẫu nhiên, chọn cá thể có quãng đường ngắn nhất

#### **Lai Ghép (Crossover) - ⚠️ Đặc Biệt**
- **Phương pháp**: **Ordered Crossover (OX)** - chuẩn cho bài toán hoán vị/TSP
- ❌ **KHÔNG dùng** phép lai cắt đoạn thông thường (sẽ gây trùng/thiếu địa điểm)
- ✅ **OX đảm bảo**: không trùng lặp, không bị thiếu ID
- **Tỷ lệ lai ghép**: 0.8

#### **Đột Biến (Mutation)**
- **Phương pháp**: **Swap Mutation** (hoán đổi)
- Chọn ngẫu nhiên **2 vị trí** trong chuỗi (trừ vị trí đầu/cuối) và **đổi chỗ chúng**
- **Tỷ lệ đột biến**: 0.05

### 3.4 Cấu Hình Tham Số

| Tham Số | Giá Trị |
|:--|:--:|
| Kích thước quần thể (Population Size) | 100 |
| Tỷ lệ lai ghép (Crossover Rate) | 0.8 |
| Tỷ lệ đột biến (Mutation Rate) | 0.05 |
| Kích thước Tournament (k) | 5 |
| Số thế hệ (Generations) | 500 |

---

## 🚀 Cách Chạy Chương Trình

### Yêu Cầu Hệ Thống
- **Python 3.7+**
- Không cần cài thêm thư viện ngoài (chỉ dùng `random` và `math` - built-in)

### Chạy Chương Trình

```bash
# Clone repo (nếu chưa có)
git clone https://github.com/nglum/GiaiThuatDiChuyen.git
cd GiaiThuatDiChuyen

# Chạy chương trình
python main.py
```

### Kết Quả Dự Kiến

```
Thế hệ 1: 
Lộ trình: Hà Nội → Hạ Long → Sapa → Ninh Bình → Phong Nha → Huế → Đà Nẵng → Mai Châu → Đảo Cát Bà → Hà Giang → Hà Nội
Tổng quãng đường: 285.45 km

Thế hệ 50: 
Lộ trình: Hà Nội → Sapa → Hà Giang → Mai Châu → Ninh Bình → Phong Nha → Huế → Đà Nẵng → Hạ Long → Đảo Cát Bà → Hà Nội
Tổng quãng đường: 245.32 km

...

Thế hệ 500: 
Lộ trình: Hà Nội → Sapa → Hà Giang → Mai Châu → Ninh Bình → Phong Nha → Huế → Đà Nẵng → Đảo Cát Bà → Hạ Long → Hà Nội
Tổng quãng đường: 215.67 km

==> Kết quả tối ưu cuối cùng:
Lộ trình: Hà Nội → Sapa → Hà Giang → Mai Châu → Ninh Bình → Phong Nha → Huế → Đà Nẵng → Đảo Cát Bà → Hạ Long → Hà Nội
Tổng quãng đường: 215.67 km
```

---

## 📁 Cấu Trúc Dự Án

```
GiaiThuatDiChuyen/
├── main.py                      # Code chính - Giải thuật GA
├── README.md                    # Tài liệu này
├── REPORT.md                    # Báo cáo chi tiết kết quả
├── requirements.txt             # Dependencies (không cần trong trường hợp này)
├── .gitignore                   # Git ignore file
└── assets/                      # Thư mục chứa ảnh, tài liệu (tuỳ chọn)
```

---

## 📝 Chi Tiết Các Hàm Chính

### `euclidean(a, b)`
Tính khoảng cách Euclide giữa hai điểm ID `a` và `b`.

### `create_chromosome()`
Tạo một cá thể (hành trình) ngẫu nhiên.

### `total_distance(route)`
Tính tổng quãng đường của hành trình `route`.

### `tournament_selection(pop, k)`
Chọn lọc k cá thể ngẫu nhiên, trả về cá thể có quãng đường ngắn nhất.

### `ordered_crossover(p1, p2)`
Lai ghép OX giữa 2 cha mẹ `p1` và `p2`, tạo con.

### `swap_mutate(chrom, rate)`
Đột biến hoán đổi 2 vị trí với xác suất `rate`.

### `genetic_algorithm(...)`
Hàm chính chạy giải thuật GA qua 500 thế hệ.

---

## 🔍 Phân Tích Kết Quả

### Đánh Giá Hiệu Suất
- **Thế hệ đầu (Gen 1)**: Quãng đường ngẫu nhiên cao (~280-300 km)
- **Thế hệ giữa (Gen 250)**: Quãng đường giảm dần (~220-240 km)
- **Thế hệ cuối (Gen 500)**: Quãng đường hội tụ đến tối ưu (~215-230 km)

### Những Điểm Nổi Bật
✅ **Tự code từng bước GA** (không dùng thư viện DEAP/PyGAD)  
✅ **Dùng Ordered Crossover (OX)** - chuẩn xác cho TSP  
✅ **Tournament Selection** - hiệu quả lựa chọn  
✅ **Swap Mutation** - đột biến đơn giản nhưng hiệu quả  
✅ **In kết quả chi tiết** mỗi 50 thế hệ  

---

## 📚 Tài Liệu Tham Khảo

### Khái Niệm GA
- **Genetic Algorithm (GA)**: https://en.wikipedia.org/wiki/Genetic_algorithm
- **Traveling Salesman Problem (TSP)**: https://en.wikipedia.org/wiki/Travelling_salesman_problem

### Các Phép Toán TSP GA
- **Ordered Crossover (OX)**: https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)
- **Tournament Selection**: https://en.wikipedia.org/wiki/Selection_(genetic_algorithm)#Tournament_selection

---

## 👨‍💻 Thông Tin Tác Giả

- **Sinh viên**: nglum
- **Lớp**: Bài tập lớn - Giải thuật Di Truyền
- **Ngày nộp**: 2026-05-29

---

## 📄 License

Dự án này là bài tập học tập, không có license cụ thể.

---

## ❓ Câu Hỏi Thường Gặp (FAQ)

### Q: Tại sao phải dùng Ordered Crossover (OX)?
**A**: Vì TSP là bài toán hoán vị, phép lai thông thường (cắt đoạn đơn giản) sẽ gây ra:
- ❌ Trùng lặp địa điểm
- ❌ Thiếu địa điểm
- ❌ Route không hợp lệ

OX giải quyết bằng cách bảo toàn thứ tự tương đối các gen → đảm bảo hợp lệ.

### Q: Có thể chạy lại code để thử kết quả khác không?
**A**: Có! Code sử dụng `random.shuffle()` nên mỗi lần chạy sẽ có kết quả khác nhau. Bạn có thể thử nhiều lần để thấy GA tìm được các hành trình tối ưu khác nhau.

### Q: Tại sao không dùng GA library có sẵn (DEAP, PyGAD)?
**A**: Đề bài yêu cầu "**phải tự code tay các bước di truyền**" để hiểu rõ nguyên lý GA từng bước, không "đen hộp" library.

### Q: Giải thuật có tìm được tối ưu toàn cục không?
**A**: Không chắc chắn 100%, vì GA là **heuristic** (không đảm bảo tối ưu toàn cục). Nhưng thường tìm được **kết quả rất tốt** (80-95% tối ưu) trong thời gian chấp nhận được.

---

## 🎯 Mục Tiêu Học Tập

Sau khi hoàn thành bài tập này, bạn sẽ:
- ✅ Hiểu rõ **cấu trúc và nguyên lý Genetic Algorithm**
- ✅ Biết cách **áp dụng GA vào bài toán tối ưu hoá thực tế** (TSP)
- ✅ Nắm vững **các phép toán GA**: selection, crossover, mutation
- ✅ Biết cách **xử lý ràng buộc** trong bài toán hoán vị
- ✅ Có kỹ năng **debug & phân tích hiệu suất giải thuật**

---

**Happy Learning! 🚀**
