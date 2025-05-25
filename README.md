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
## I. Về dự án:
- `Data`: Bao gồm những dữ liệu đã thu thập được trong quá trình xây dựng dự án
- `Images`: Bao gồm ảnh có trong dự án
- `Model`: Bác mô hình được xuất ra trong quá trình xây dựng dự án
- `Scource`: Code của dự án, cụ thể:
   + `Source/cawl_product_id.py`: File này thu thập id của các sản phẩm.
   + `Source/cawl_comment.py`: Sử dụng id đã thu thập được thu thập dữ liệu feedback của khách hàng.
   + `Source/a_preprocessing_and_KNN_Sentiment.ipynb`: Từ dữ liệu thi thập được, tiến hành xử lý và huấn luyện mô hình KNN.
   + `Source/model_Random_Forest_Sentiment.ipynb`: Xử lý và huấn luyện mô hình Random Forest.
   + `Source/model_LSTM_Sentiment.ipynb`: Xử lý và huấn luyện mô hình LSTM.
Chi tiết xin mời xem tiếp trong từng file. 
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
