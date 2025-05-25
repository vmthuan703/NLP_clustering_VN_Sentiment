# Ứng dụng Machine Learning & Deep Learning để xây dựng mô hình phân tích cảm xúc của khách hàng dựa trên các bình luận nhằm xác định và hỗ trợ xây dựng chiến lược kinh doanh
Dự án này bao gồm việc thu thập dữ liệu của hơn 10.000 bình luận trong các danh mục về điện thoại & phụ kiện điện thoại trên tiki.vn. Sau đó khám phá dữ liệu và xây dựng mô hình, cụ thể:
- Thu thập dữ liệu:
  + Trước tiên thu thập id của hơn 600 sản phẩm tại sàn thương mại điện tử Tiki (https://tiki.vn/),
  + Từ id của hơn 600 sản phẩm đó, tiếp tục thu thập dữ liệu về feedback của gần 35.000 khách hàng về sản phẩm,
  + Lưu dữ liệu về file csv.
- Tiền xử lý dữ liệu
  + Làm sạch văn bản (loại bỏ stopwords, ký tự đặc biệt, emoji,…), tokenization, loại bỏ stop words...
  + Gán nhãn cảm xúc,
  + Biểu diễn văn bản (VTF-IDF vectorization, Tokenization + Padding),
  + Xử lý mất cân bằng nhãn.
- Trực quan hoá dữ liệu:
- Xây dựng mô hình Học máy, Học sâu (KNN, Random Forest, LSTM):
  + Xây dựng mô hình phân tích cảm xúc của khách hàng dựa trên các bình luận,
  + Đánh giá hiệu xuất mô hình,
  + Đưa ra phương hướng cải thiện.
## I.Thông tin về tập dữ liệu:
34808 dòng,
8 cột bao gồm:
- title: Tiêu đề comment của khách hàng
- content: Nội dung comment của khách hàng
- thank_count: Số phẩn hồi tích cực về comment đó
- customer_id: id của khách hàng đã comment
- rating: số sao mà khách hàng đánh giá về sản phẩm (1-5 sao)
- created_at: Ngày comment
- customer_name: Tên của khách hàng
- purchased_at: Ngày mua hàng
## II.Thư viện sử dụng
- Pandas
- Numpy
- Matplotlib
- Time
- Random
- Requests
- Regex
- Underthesea
- Sklearn
- Imblearn
- Tensorflow
- Keras
## III. Tham khảo
- https://www.youtube.com/watch?v=4ANrdE3FDPw&t=1858s
- https://github.com/ZeusCoderBE
