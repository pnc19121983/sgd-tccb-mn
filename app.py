import streamlit as st
import pandas as pd
import os
from datetime import datetime

# -------------------------------
# 1️⃣ Dữ liệu xã / trường
# -------------------------------
schools = {
    "Xã Lâm Bình": [
        "Nhóm trẻ Hoa Mai",
        "Trường Mầm Non Xuân Lập",
        "Trường Mầm Non Phúc Yên",
        "Trường Mầm Non Lăng Can"
    ],
    "Xã Thượng Lâm": [
        "Trường Mầm Non Khuôn Hà",
        "Trường Mầm Non Thượng Lâm"
    ],
    "Xã Bình An": [
        "Trường Mầm Non Thổ Bình",
        "Nhóm trẻ Họa Mi",
        "Trường Mầm Non Bình An"
    ],
    "Xã Minh Quang": [
        "Nhóm trẻ Hoa Hướng Dương",
        "Trường Mầm Non Minh Quang",
        "Trường Mầm Non Hồng Quang",
        "Trường Mầm Non Phúc Sơn",
        "Nhóm trẻ Minh Sơn"
    ],
    "Xã Nà Hang": [
        "Nhóm trẻ Ngôi Sao Nhỏ - Na Hang",
        "Trường MN Năng Khả",
        "Trường MN Thanh Tương",
        "Trường MN Hoa Mai",
        "Nhóm trẻ Hoa Hồng - Na Hang"
    ],
    "Xã Hồng Thái": [
        "Trường MN Đà Vị",
        "Trường MN Sơn Phú",
        "Trường MN Hồng Thái"
    ],
    "Xã Yên Hoa": [
        "Trường MN Yên Hoa",
        "Trường MN Khâu Tinh"
    ],
    "Xã Thượng Nông": [
        "Trường MN Thượng Nông",
        "Trường MN Thượng Giáp"
    ],
    "Xã Côn Lôn": [
        "Trường MN Côn Lôn",
        "Trường MN Sinh Long"
    ],
    "Xã Chiêm Hóa": [
        "Nhóm trẻ Hoa Hồng",
        "Nhóm trẻ Hoa Hướng Dương",
        "Nhóm trẻ độc lập Summer Sun",
        "Nhóm trẻ độc lập Thiên Thần Nhỏ",
        "Trường MN Ngọc Hội",
        "Trường MN Phúc Thịnh",
        "Nhóm trẻ Bình An (Vĩnh Lộc)",
        "Nhóm trẻ Bình Minh (Vĩnh Lộc)",
        "Trường MN Trung Hòa",
        "Trường Mầm non Xuân Quang",
        "Trường MN Sao Mai"
    ],
        "Xã Kim Bình": [
        "Nhóm trẻ Tuổi Thơ Xanh- Vinh Quang",
        "Trường MN Vinh Quang",
        "Trường MN Kim Bình",
        "Trường MN Bình Nhân",
        "Nhóm trẻ Bình Minh (Kim Bình)"
    ],
    "Xã Tri Phú": [
        "Trường MN Linh Phú",
        "Trường MN Tri Phú"
    ],
    "Xã Kiên Đài": [
        "Nhóm trẻ Họa Mi - Phú Bình",
        "Trường MN Phú Bình",
        "Trường MN Kiên Đài"
    ],
    "Xã Yên Lập": [
        "Trường MN Yên Lập",
        "Trường MN Bình Phú"
    ],
    "Xã Tân An": [
        "Trường MN Hà Lang",
        "Trường MN Tân An"
    ],
    "Xã Hòa An": [
        "Trường MN Tân Thịnh",
        "Trường MN Nhân Lý",
        "Trường MN Hòa An"
    ],
    "Xã Yên Nguyên": [
        "Trường MN Yên Nguyên",
        "Nhóm trẻ Bình Minh - Yên Nguyên",
        "Trường MN Hòa Phú",
        "Nhóm trẻ Nắng Mai - Xã Yên Nguyên"
    ],
    "Xã Trung Hà": [
        "Trường MN Trung Hà"
    ],
    "Xã Tân Mỹ": [
        "Trường MN Tân Mỹ",
        "Trường MN Hùng Mỹ"
    ],
    "Xã Hàm Yên": [
        "Nhóm trẻ Bình Minh",
        "Trường Mầm Non Bằng Cốc",
        "Nhóm trẻ Siêu Chip",
        "Trường Mầm Non Tân Thành",
        "Trường Mầm Non Nhân Mục",
        "Nhóm trẻ Ngôi Nhà Hạnh Phúc",
        "Trường Mầm Non Tân Yên"
    ],
        "Xã Bạch Xa": [
        "Trường Mầm Non Yên Thuận",
        "Trường Mầm Non Minh Khương",
        "Trường Mầm non Bạch Xa"
    ],
    "Xã Phù Lưu": [
        "Trường Mầm Non Minh Dân",
        "Trường Mầm Non Phù Lưu"
    ],
    "Xã Bình Xa": [
        "Trường Mầm non Bình Xa",
        "Trường Mầm Non Minh Hương"
    ],
    "Xã Yên Phú": [
        "Trường mầm Non Yên Lâm",
        "Trường Mầm Non Yên Phú"
    ],
    "Xã Thái Sơn": [
        "Trường mầm Non Thái Sơn",
        "Trường mầm Non Thành Long"
    ],
    "Xã Thái Hòa": [
        "Trường Mầm Non Đức Ninh",
        "Trường Mầm Non Thái Hòa"
    ],
    "Xã Hùng Đức": [
        "Trường mầm non Hùng Đức"
    ],
    "Xã Yên Sơn": [
        "Trường mầm non Tứ Quận",
        "Trường mầm non Chân Sơn",
        "Trường mầm non Thắng Quân",
        "Trường mầm non Lang Quán"
    ],
    "Xã Hùng Lợi": [
        "Trường mầm non Trung Minh",
        "Trường mầm non Hùng Lợi"
    ],
    "Xã Kiến Thiết": [
        "Trường MN Kiến Thiết"
    ],
    "Xã Lực Hành": [
        "Trường mầm non Quý Quân",
        "Trường mầm non Chiêu Yên",
        "Trường mầm non Lực Hành"
    ],
    "Xã Nhữ Khê": [
        "Trường MN Nhữ Hán",
        "Trường mầm non Nhữ Khê",
        "Trường MN Đội Bình",
        "Trường MN Hoa Phượng - Z129"
    ],
    "Xã Tân Long": [
        "Trường mầm non Tân Long",
        "Trường mầm non Tân Tiến"
    ],
    "Xã Thái Bình": [
        "Trường mầm non Phú Thịnh",
        "Trường mầm non Thái Bình",
        "Trường mầm non Tiến Bộ"
    ],
    "Xã Trung Sơn": [
        "Trường mầm non Công Đa",
        "Trường mầm non Trung Sơn",
        "Trường mầm non Đạo Viện"
    ],
    "Xã Xuân Vân": [
        "Trường mầm non Xuân Vân",
        "Trường mầm non Phúc Ninh",
        "Trường mầm non Trung Trực"
    ],
    "Xã Sơn Dương": [
        "Trường MN Hoa Trạng Nguyên",
        "Nhóm trẻ An Kỳ",
        "Trường MN Hoa Sen",
        "Trường MN Tú Thịnh",
        "Trường MN Hoa Hồng",
        "Trường MN Phúc Ứng",
        "Trường MN Hợp Thành"
    ],
    "Xã Tân Trào": [
        "Trường mầm non Kim Quan",
        "Trường MN Tân Trào",
        "Trường MN Trung Yên"
    ],
    "Xã Minh Thanh": [
        "Trường MN Lương Thiện",
        "Trường MN Bình Yên",
        "Trường MN Minh Thanh",
        "Nhóm trẻ Huyền Linh"
    ],
    "Xã Bình Ca": [
        "Nhóm trẻ Ân Phúc",
        "Trường MN Cấp Tiến",
        "Nhóm trẻ Phượng Hồng",
        "Trường MN Vĩnh Lợi",
        "Trường MN Thượng Ấm",
        "Nhóm trẻ Hoa Mặt Trời"
    ],
    "Xã Tân Thanh": [
        "Trường MN Kháng Nhật",
        "Trường MN Tân Thanh",
        "Trường MN Hợp Hòa"
    ],
    "Xã Sơn Thủy": [
        "Trường MN Ninh Lai",
        "Trường MN Thiện Kế",
        "Trường MN Sơn Nam",
        "Nhóm trẻ tư thục Sen Hồng"
    ],
    "Xã Phú Lương": [
        "Trường MN Đại Phú",
        "Trường MN Tam Đa",
        "Trường MN Phú Lương"
    ],
    "Xã Trường Sinh": [
        "Trường MN Hào Phú",
        "Trường MN Đông Lợi",
        "Trường MN Trường Sinh"
    ],
    "Xã Hồng Sơn": [
        "Trường MN Hồng Lạc",
        "Trường MN Chi Thiết",
        "Trường MN Vân Sơn",
        "Trường MN Văn Phú"
    ],
    "Xã Đông Thọ": [
        "Trường MN Đồng Quý",
        "Trường MN Đông Thọ 2",
        "Trường MN Đông Thọ",
        "Trường MN Quyết Thắng"
    ],
    "Phường Minh Xuân": [
        "Trường MN Pony",
        "Nhóm Ban Mai Xanh CS1",
        "Nhóm Ban Mai Xanh CS3",
        "Nhóm Những Em Bé Hạnh Phúc 3",
        "Nhóm CASA Montessori",
        "Nhóm Ban Mai Xanh CS5",
        "Sao Biển",
        "Nhóm Montessori 3",
        "Nhóm Ban Mai Xanh CS6",
        "Nhóm Những Em Bé Hạnh Phúc",
        "Nhóm Những Em Bé Hạnh Phúc 2",
        "Mặt Trời Nhỏ",
        "Lớp MN độc lập Ngôi Sao Việt",
        "Trường MN Ỷ La",
        "Trường MN Tân Hà",
        "Tinh Hoa Steam Bé Bé",
        "Trường MN Sao Mai TP",
        "Trường MN Hoa Sen TP",
        "Trường MN Phan Thiết",
        "Trường MN Hoa Mai TP",
        "Trường MN Hoa Hồng TP",
        "Trường MN Tân Trào - Tuyên Quang",
        "Trường MN Trung Môn",
        "Trường MN Kim Phú",
        "Nhóm Ban Mai Xanh CS2",
        "Nhóm Ban Mai Xanh CS4",
        "Nhóm Montessori 2",
        "Nhóm Montessori 1"
    ],
    "Phường An Tường": [
        "Trường MN An Khang",
        "Trường MN Hoa Phượng",
        "Trường MN Sông Lô",
        "Trường MN Lưỡng Vượng",
        "Trường MN Hưng Thành",
        "Trường mầm non Hoàng Khai",
        "Trường MN Bình Minh",
        "Xuka Montessori",
        "Ngôi Nhà Montessori 2"
    ],
    "Phường Bình Thuận": [
        "Trường MN Đội Cấn",
        "Trường MN Tân Bình",
        "Trường MN Thái Long"
    ],
    "Phường Nông Tiến": [
        "Trường MN Tràng Đà",
        "Trường MN Nông Tiến",
        "Trường MN Hương Sen"
    ],
        "Phường Mỹ Lâm": [
        "Trường MN Phú Lâm",
        "Trường mầm non Mỹ Bằng",
        "Nhóm trẻ Hoa Phượng",
        "Nhóm trẻ Anh Dương",
        "Trường mầm non Đình Bằng"
    ],
    "Xã Đồng Văn": [
        "Trường MN Tả Lủng",
        "Trường Mầm non Pải Lủng",
        "Trường mầm non Đồng Văn",
        "Trường MN Thài Phìn Tủng",
        "Trường Mầm non Tả Phìn"
    ],
    "Xã Lũng Cú": [
        "Trường Mầm non Lũng Táo",
        "Trường Mầm non Ma Lé",
        "Trường Mầm non Lũng Cú"
    ],
    "Xã Sà Phìn": [
        "Trường Mầm non Sủng Là",
        "Trường MN Sà Phìn",
        "Trường MN Sảng Tủng",
        "Trường Mầm non Sính Lủng"
    ],
    "Xã Phố Bảng": [
        "Trường Mầm non Phố Là",
        "Trường Mầm non Lũng Thầu",
        "Trường MN Phố Cáo",
        "Trường MN Phố Bảng"
    ],
    "Xã Lũng Phìn": [
        "Trường Mầm non Hố Quáng Phìn",
        "Trường Mầm non Lũng Phìn",
        "Trường Mầm non Sủng Trái"
    ],
    "Xã Mèo Vạc": [
        "Nhóm nhà trẻ Mai Hồng",
        "Trường MN Hoa Đào",
        "Trường Mầm non Tả Lủng",
        "Trường Mầm non Hoa Lan",
        "Trường Mầm non Pả Vi",
        "Trường Mầm non Giàng Chu Phìn",
        "Nhóm trẻ tư thục Đô Rê Mon"
    ],
    "Xã Sủng Máng": [
        "Trường Mầm non Sủng Trà",
        "Trường Mầm non Lũng Chinh",
        "Trường MN Sủng Máng"
    ],
    "Xã Sơn Vĩ": [
        "Trường Mầm non Sơn Vĩ",
        "Trường Mầm non Thượng Phùng",
        "Trường MN Xín Cái"
    ],
    "Xã Khâu Vai": [
        "Trường Mầm non Lũng Pù",
        "Trường Mầm non Khâu Vai",
        "Trường Mầm non Cán Chu Phìn"
    ],
    "Xã Niêm Sơn": [
        "Trường Mầm non Niêm Sơn",
        "Trường Mầm non Niêm Tòng"
    ],
    "Xã Tát Ngà": [
        "Trường Mầm non Tát Ngà",
        "Trường Mầm non Nậm Ban"
    ],
    "Xã Yên Minh": [
        "Trường MN Vần Chải",
        "Trường Mầm non Đông Minh",
        "Trường Mầm non Lao Và Chải",
        "Trường Mầm non Hoa Hồng",
        "Nhóm trẻ tư thục Hoa Phượng",
        "Trường MN Hữu Vinh"
    ],
    "Xã Thắng Mố": [
        "Trường Mầm non Sủng Thài",
        "Trường Mầm non Sủng Cháng",
        "Trường Mầm non Thắng Mố"
    ],
    "Xã Bạch Đích": [
        "Trường Mầm non Na Khê",
        "Trường Mầm non Bạch Đích",
        "Trường Mầm non Phú Lũng"
    ],
    "Xã Mậu Duệ": [
        "Trường MN Mậu Long",
        "Trường Mầm non Mậu Duệ",
        "Mầm non Ngam La"
    ],
    "Xã Ngọc Long": [
        "Trường Mầm non Ngọc Long"
    ],
    "Xã Du Già": [
        "Trường MN Du Già",
        "Trường Mầm non Du Tiến"
    ],
    "Xã Đường Thượng": [
        "Trường Mầm non Đường Thượng",
        "Trường Mầm non Lũng Hồ"
    ],
    "Xã Quản Bạ": [
        "Trường Mầm non Quyết Tiến",
        "Trường Mầm non Quản Bạ",
        "Trường Mầm non Tam Sơn"
    ],
        "Xã Lùng Tám": [
        "Trường Mầm non Thái An",
        "Trường Mầm non Đông Hà",
        "Trường Mầm non Lùng Tám"
    ],
    "Xã Cán Tỷ": [
        "Trường Mầm non Cán Tỷ",
        "Trường Mầm non Bát Đại Sơn"
    ],
    "Xã Nghĩa Thuận": [
        "Trường Mầm non Thanh Vân",
        "Trường Mầm non Nghĩa Thuận"
    ],
    "Xã Tùng Vài": [
        "Trường Mầm non Cao Mã Pờ",
        "Trường Mầm non Tùng Vài",
        "Trường Mầm non Tả Ván"
    ],
    "Xã Bắc Mê": [
        "Trường mầm non Yên Phú",
        "Trường Mầm non Lạc Nông",
        "Trường Mầm non Hoa Sen",
        "Trường Mầm non Yên Phong"
    ],
    "Xã Yên Cường": [
        "Trường Mầm non Yên Cường",
        "Trường Mầm non Phiêng Luông"
    ],
    "Xã Đường Hồng": [
        "Trường Mầm non Đường Âm",
        "Trường Mầm non Phú Nam",
        "Trường Mầm non Đường Hồng"
    ],
    "Xã Giáp Trung": [
        "Trường Mầm non Giáp Trung"
    ],
    "Xã Minh Sơn": [
        "Trường Mầm non Minh Sơn"
    ],
    "Xã Minh Ngọc": [
        "Trường MN Thượng Tân",
        "Trường Mầm non Minh Ngọc"
    ],
    "Xã Ngọc Đường": [
        "Trường Mầm non Ngọc Đường",
        "Trường Mầm non Yên Định"
    ],
    "Phường Hà Giang 1": [
        "Lớp Mầm non Đồ Rê Mí (cơ sở 2)",
        "Trường Mầm non Hoa Sen",
        "Lớp Mầm non Ngôi Sao Xanh (cơ sở 2)",
        "Trường Mầm non Hướng Dương",
        "Trường Mầm non Phương Độ",
        "Trường Mầm non Phương Thiện",
        "Trường Mầm non Phương Thanh",
        "Trường Mầm Non Họa Mi",
        "Nhóm trẻ Hoa Phượng Đỏ",
        "Lớp mầm non Em bé hạnh phúc (cơ sở 2)"
    ],
    "Phường Hà Giang 2": [
        "Nhóm trẻ Em Bé Hạnh Phúc",
        "Trường MN Star academy",
        "Nhóm trẻ Mặt Trời Nhỏ",
        "Trường Mầm non Sơn Ca",
        "Trường MN Sao Mai",
        "Nhóm trẻ tư thục Ngôi Sao Xanh",
        "Trường Mầm non Hoa lan",
        "Nhóm trẻ Ngôi Sao Nhỏ",
        "Trường MN Nụ cười hạnh phúc",
        "Lớp mầm non Đồ Rê Mí",
        "Lớp mầm non độc lập Đồ Rê Mí (cơ sở 3)",
        "Nhóm Trẻ Tư Thục Bông Sen",
        "Trường Mầm non Phong Quang",
        "Lớp Mầm non độc lập Hoa Bé Ngoan",
        "Trường Mầm non Hoa Hồng",
        "Trường Mầm non Hoa Mai",
        "Trường Mầm non Quang Trung",
        "Trường MN Hoa Đào",
        "Trường Mầm non Hoa Lê",
        "Lớp Mầm non Happy Day",
        "Nhóm trẻ Mẹ và Bé"
    ],
    "Xã Vị Xuyên": [
        "Mầm non DORAEMON",
        "Trường Mầm Non Sơn Ca",
        "Sunny",
        "Trường Mầm non Hoa Mai",
        "Trường Mầm non Họa Mi",
        "Trường Mầm Non Đạo Đức"
    ],
    "Xã Lao Chải": [
        "Trường MN Thanh Đức",
        "Trường Mầm Non Lao Chải"
    ],
    "Xã Thanh Thủy": [
        "Trường Mầm non Phương Tiến",
        "Trường Mầm non Thanh Thủy"
    ],
    "Xã Minh Tân": [
        "Trường Mầm non Minh Tân"
    ],
    "Xã Thuận Hòa": [
        "Trường Mầm Non Hướng Dương",
        "Trường Mầm non Thuận Hòa"
    ],
    "Xã Tùng Bá": [
        "Trường MN Tùng Bá"
    ],
    "Xã Phú Linh": [
        "Trường Mầm non Kim Linh",
        "Trường Mầm non Phú Linh",
        "Trường Mầm non Kim Thạch"
    ],
    "Xã Linh Hồ": [
        "Trường Mầm non Ngọc Linh",
        "Trường Mầm Non Linh Hồ",
        "Trường Mầm non Trung Thành"
    ],
    "Xã Bạch Ngọc": [
        "Trường Mầm non Ngọc Minh",
        "Trường Mầm non Bạch Ngọc"
    ],
    "Xã Việt Lâm": [
        "Trường Mầm non Việt Lâm",
        "Trường Mầm non Quảng Ngần"
    ],
    "Xã Cao Bồ": [
        "Trường Mầm non Cao Bồ"
    ],
    "Xã Thượng Sơn": [
        "Trường MN Thượng Sơn"
    ],
    "Xã Bắc Quang": [
        "Trường Mầm non Việt Quang I",
        "Trường MN Hoa Mai",
        "Trường Mầm non Việt Vinh",
        "Trường Mầm non Quang Minh",
        "Trường Mầm non Việt Quang II",
        "Nhóm trẻ tư thục Tuổi Thơ",
        "Nhóm trẻ tư thục Hoa Hồng",
        "Nhóm trẻ tư thục Baby Shark",
        "Lớp Mẫu giáo độc lập Học Viên Nhí"
    ],
    "Xã Tân Quang": [
        "Trường Mầm non Tân Thành",
        "Trường Mầm non Tân Lập",
        "Trường Mầm non Tân Quang"
    ],
    "Xã Đồng Tâm": [
        "Trường Mầm non Đồng Tâm",
        "Trường Mầm non Đồng Tiến",
        "Trường Mầm non Thượng Bình"
    ],
    "Xã Liên Hiệp": [
        "Trường Mầm non Hữu Sản",
        "Trường Mầm non Liên Hiệp",
        "Trường Mầm non Đức Xuân"
    ],
    "Xã Bằng Hành": [
        "Trường Mầm non Vô Điếm",
        "Trường Mầm non Kim Ngọc",
        "Trường Mầm non Bằng Hành"
    ],
        "Xã Hùng An": [
        "Trường Mầm non Việt Hồng",
        "Trường Mầm non Hùng An",
        "Trường Mầm non Tiên Kiều",
        "Nhóm trẻ độc lập tư thục Ban Mai"
    ],
    "Xã Vĩnh Tuy": [
        "Trường Mầm non Đông Thành",
        "Trường Mầm non Vĩnh Tuy",
        "Trường Mầm non Sơn Ca"
    ],
    "Xã Đồng Yên": [
        "Trường Mầm non Vĩnh Phúc",
        "Trường Mầm non Đồng Yên"
    ],
    "Xã Quang Bình": [
        "Trường Mầm non Tân Nam",
        "Trường Mầm non Yên Bình",
        "Mầm Non Sao Mai"
    ],
    "Xã Tiên Yên": [
        "Trường Mầm non Tiên Yên",
        "Trường Mầm non Hương Sơn",
        "Trường Mầm non Vĩ Thượng"
    ],
    "Xã Xuân Giang": [
        "Trường Mầm non Nà Khương",
        "Trường Mầm non Xuân Giang"
    ],
    "Xã Bằng Lang": [
        "Trường Mầm non Yên Hà",
        "Trường Mầm non Bằng Lang"
    ],
    "Xã Yên Thành": [
        "Trường Mầm non Yên Thành",
        "Trường Mầm non Bản Rịa"
    ],
    "Xã Tân Trịnh": [
        "Trường Mầm non Tân Bắc",
        "Trường Mầm non Tân Trịnh"
    ],
    "Xã Tiên Nguyên": [
        "Trường Mầm non Tiên Nguyên"
    ],
    "Xã Hoàng Su Phì": [
        "Trường Mầm non Tụ Nhân",
        "Trường Mầm non Đản Ván",
        "Trường Mầm non Bản Luốc",
        "Trường Mầm non Ngàm Đăng Vài",
        "Trường Mầm non Vinh Quang"
    ],
    "Xã Thông Nguyên": [
        "Trường Mầm non Xuân Minh",
        "Trường Mầm non Thông Nguyên"
    ],
    "Xã Hồ Thầu": [
        "Trường Mầm non Hồ Thầu",
        "Trường Mầm non Nậm Khòa",
        "Trường Mầm non Nam Sơn"
    ],
    "Xã Nậm Dịch": [
        "Trường Mầm non Nậm Ty",
        "Trường Mầm non Nậm Dịch",
        "Trường Mầm non Tả Sử Chóong"
    ],
    "Xã Tân Tiến": [
        "Trường Mầm non Bản Nhùng",
        "Trường Mầm non Tân Tiến",
        "Trường Mầm non Túng Sán"
    ],
    "Xã Thàng Tín": [
        "Trường Mầm non Thàng Tín",
        "Trường MN Thèn Chu Phìn",
        "Trường Mầm non Pố Lồ"
    ],
    "Xã Bản Máy": [
        "Trường Mầm non Bản Phùng",
        "Trường Mầm non Chiến Phố",
        "Trường Mầm non Bản Máy"
    ],
    "Xã Pờ Ly Ngài": [
        "Trường Mầm non Sán Sả Hồ",
        "Trường Mầm non Pờ Ly Ngài",
        "Trường Mầm non Nàng Đôn"
    ],
    "Xã Xín Mần": [
        "Trường Mầm non Xín Mần",
        "Trường Mầm Non Chí Cà",
        "Trường Mầm Non Nàn Xỉn",
        "Trường Mầm non Bản Díu",
        "Trường Mầm Non Thèn Phàng"
    ],
    "Xã Pà Vầy Sủ": [
        "Trường Mầm non Bản Ngò",
        "Trường Mầm non Hoa Mai",
        "Trường Mầm non Nàn Ma",
        "Trường Mầm non Hoa Sen",
        "Trường Mầm non Pà Vầy Sủ"
    ],
    "Xã Nấm Dẩn": [
        "Trường Mầm non Nấm Dẩn",
        "Trường Mầm non Tả Nhìu",
        "Trường MN Chế Là"
    ],
    "Xã Trung Thịnh": [
        "Trường Mầm non Thu Tà",
        "Trường MN Trung Thịnh",
        "Trường Mầm non Cốc Rế"
    ],
    "Xã Quảng Nguyên": [
        "Mầm non Quảng Nguyên"
    ],
    "Xã Khuôn Lùng": [
        "Trường MN Khuôn Lùng",
        "Trường Mầm non Nà Chì"
    ],
}

# -------------------------------
# 2️⃣ File lưu dữ liệu
# -------------------------------
DATA_FILE = "dulieu.csv"
STATUS_FILE = "danhsach.csv"

# -------------------------------
# 3️⃣ Khởi tạo file nếu chưa có
# -------------------------------
def init_status_file():
    data_list = []
    for xa, truongs in schools.items():
        for truong in truongs:
            data_list.append({"Xã": xa, "Trường": truong, "Đã nhập": False})
    pd.DataFrame(data_list).to_csv(STATUS_FILE, index=False, encoding="utf-8-sig")

if not os.path.exists(STATUS_FILE):
    init_status_file()

status_df = pd.read_csv(STATUS_FILE)

# -------------------------------
# 4️⃣ Cấu hình giao diện
# -------------------------------
st.set_page_config(page_title="Hệ thống nhập liệu trường học", page_icon="🏫", layout="centered")
st.title("🏫 THỐNG KÊ SỐ LIỆU CẤP MẦM NON")

# -------------------------------
# -------------------------------
# 5️⃣ Form nhập liệu theo bước
# -------------------------------
st.markdown("### Bước 1: Chọn xã/phường")
xa_selected = st.selectbox("Chọn xã/phường:", ["-- Chọn xã --"] + list(status_df["Xã"].unique()))

if xa_selected != "-- Chọn xã --":
    st.markdown("### Bước 2: Chọn trường")

    truong_options = status_df[
        (status_df["Xã"] == xa_selected) & (status_df["Đã nhập"] == False)
    ]["Trường"].tolist()

    if not truong_options:
        st.info("✅ Tất cả các trường trong xã này đã nhập xong.")
    else:
        truong_selected = st.selectbox("Chọn trường:", ["-- Chọn trường --"] + truong_options)

        if truong_selected != "-- Chọn trường --":
            st.markdown("### Bước 3: Nhập nội dung chi tiết")

            # =======================
            # PHẦN 1
            # =======================
            st.subheader("📘 Phần 1. Số lớp, số học sinh năm học 2025-2026")

            so_diem_truong = st.number_input("Số điểm trường:", min_value=0, step=1)
            tong_lop_nha_tre = st.number_input("Tổng số lớp Nhà trẻ:", min_value=0, step=1)
            tong_lop_mau_giao = st.number_input("Tổng số lớp Mẫu giáo:", min_value=0, step=1)
            tong_tre_nha_tre = st.number_input("Tổng số trẻ Nhà trẻ:", min_value=0, step=1)
            tong_tre_mau_giao = st.number_input("Tổng số trẻ Mẫu giáo:", min_value=0, step=1)

            st.markdown("**Chi tiết lớp:**")
            lop_2_12 = st.number_input("Số lớp nhà trẻ từ 2-12 tháng tuổi:", min_value=0, step=1)
            lop_12_24 = st.number_input("Số lớp nhà trẻ từ 12-24 tháng tuổi:", min_value=0, step=1)
            lop_24_36 = st.number_input("Số lớp nhà trẻ từ 24-36 tháng tuổi:", min_value=0, step=1)
            lop_3_4 = st.number_input("Số lớp mẫu giáo từ 3-4 tuổi:", min_value=0, step=1)
            lop_4_5 = st.number_input("Số lớp mẫu giáo từ 4-5 tuổi:", min_value=0, step=1)
            lop_5_6 = st.number_input("Số lớp mẫu giáo từ 5-6 tuổi:", min_value=0, step=1)

            # =======================
            # PHẦN 2
            # =======================
            st.subheader("📗 Phần 2. Số được giao năm 2025")

            so_duoc_giao = {
                "Lãnh đạo QL": st.number_input("Lãnh đạo QL (giao):", min_value=0, step=1),
                "GV nhà trẻ": st.number_input("Giáo viên nhà trẻ (giao):", min_value=0, step=1),
                "GV mẫu giáo": st.number_input("Giáo viên mẫu giáo (giao):", min_value=0, step=1),
                "Kế toán": st.number_input("Kế toán (giao):", min_value=0, step=1),
                "Văn thư": st.number_input("Văn thư (giao):", min_value=0, step=1),
                "Thủ quỹ": st.number_input("Thủ quỹ (giao):", min_value=0, step=1),
                "Thư viện": st.number_input("Thư viện (giao):", min_value=0, step=1),
                "Hỗ trợ phục vụ (HĐ111)": st.number_input("Hỗ trợ phục vụ (HĐ111 - giao):", min_value=0, step=1),
                "Chuyên môn nghiệp vụ (HĐ111)": st.number_input("Chuyên môn nghiệp vụ (HĐ111 - giao):", min_value=0, step=1),
            }

            # =======================
            # PHẦN 3
            # =======================
            st.subheader("📙 Phần 3. Số có mặt đến 01/11/2025")

            so_co_mat = {
                "Lãnh đạo QL": st.number_input("Lãnh đạo QL (có mặt):", min_value=0, step=1),
                "GV nhà trẻ": st.number_input("Giáo viên nhà trẻ (có mặt):", min_value=0, step=1),
                "GV mẫu giáo": st.number_input("Giáo viên mẫu giáo (có mặt):", min_value=0, step=1),
                "Kế toán": st.number_input("Kế toán (có mặt):", min_value=0, step=1),
                "Văn thư": st.number_input("Văn thư (có mặt):", min_value=0, step=1),
                "Thủ quỹ": st.number_input("Thủ quỹ (có mặt):", min_value=0, step=1),
                "Thư viện": st.number_input("Thư viện (có mặt):", min_value=0, step=1),
                "Hỗ trợ phục vụ (HĐ111)": st.number_input("Hỗ trợ phục vụ (HĐ111 - có mặt):", min_value=0, step=1),
                "Chuyên môn nghiệp vụ (HĐ111)": st.number_input("Chuyên môn nghiệp vụ (HĐ111 - có mặt):", min_value=0, step=1),
            }

            # =======================
            # LƯU DỮ LIỆU
            # =======================
            if st.button("💾 Lưu dữ liệu"):
                new_row = {
                    "Xã": xa_selected,
                    "Trường": truong_selected,
                    # --- Phần 1 ---
                    "Số điểm trường": so_diem_truong,
                    "Tổng lớp nhà trẻ": tong_lop_nha_tre,
                    "Tổng lớp mẫu giáo": tong_lop_mau_giao,
                    "Tổng trẻ nhà trẻ": tong_tre_nha_tre,
                    "Tổng trẻ mẫu giáo": tong_tre_mau_giao,
                    "Lớp 2-12 tháng": lop_2_12,
                    "Lớp 12-24 tháng": lop_12_24,
                    "Lớp 24-36 tháng": lop_24_36,
                    "Lớp 3-4 tuổi": lop_3_4,
                    "Lớp 4-5 tuổi": lop_4_5,
                    "Lớp 5-6 tuổi": lop_5_6,
                    # --- Phần 2 & 3 ---
                    **{f"{k} (giao)": v for k, v in so_duoc_giao.items()},
                    **{f"{k} (có mặt)": v for k, v in so_co_mat.items()},
                    "Ngày nhập": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                if os.path.exists(DATA_FILE):
                    df = pd.read_csv(DATA_FILE)
                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                else:
                    df = pd.DataFrame([new_row])
                df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")

                status_df.loc[
                    (status_df["Xã"] == xa_selected) & (status_df["Trường"] == truong_selected),
                    "Đã nhập"
                ] = True
                status_df.to_csv(STATUS_FILE, index=False, encoding="utf-8-sig")

                st.success(f"✅ Đã lưu dữ liệu cho **{truong_selected}**.")
                st.balloons()


# -------------------------------
# 6️⃣ Khu vực admin ở phía dưới form
# -------------------------------
st.markdown("---")
st.subheader("🔐 Dành cho quản trị viên")

ADMIN_PASSWORD = "12345"  # 👉 đổi mật khẩu ở đây

# Trạng thái đăng nhập admin
if "admin" not in st.session_state:
    st.session_state.admin = False

if not st.session_state.admin:
    password = st.text_input("Nhập mật khẩu admin:", type="password")
    if st.button("Đăng nhập"):
        if password == ADMIN_PASSWORD:
            st.session_state.admin = True
            st.success("✅ Đăng nhập thành công!")
            st.rerun()
        else:
            st.error("❌ Sai mật khẩu, vui lòng thử lại.")
else:
    st.success("👑 Bạn đang ở chế độ quản trị.")

    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)

        st.markdown("### 🧮 Dữ liệu đã nhập")
        st.dataframe(df)

        # Tổng hợp
        st.markdown("### 📊 Thống kê theo xã")
        summary = df.groupby("Xã")[["Số học sinh", "Số giáo viên", "Số phòng học"]].sum()
        st.dataframe(summary)

        # Xuất Excel
        export_name = f"tonghop_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        df.to_excel(export_name, index=False)

        with open(export_name, "rb") as f:
            st.download_button(
                label="⬇️ Tải về file Excel",
                data=f,
                file_name=export_name,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning("⚠️ Chưa có dữ liệu nào được nhập.")

    # 🔄 Nút reset toàn bộ dữ liệu
    st.markdown("### ⚠️ Reset toàn bộ dữ liệu")
    st.warning("Thao tác này sẽ xóa toàn bộ dữ liệu đã nhập và đặt lại danh sách trường về trạng thái ban đầu!")

    if st.button("🔄 Reset dữ liệu"):
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)
        init_status_file()
        st.success("✅ Đã reset toàn bộ dữ liệu và danh sách trường về trạng thái ban đầu.")
        st.rerun()

    # Nút đăng xuất
    if st.button("🚪 Đăng xuất"):
        st.session_state.admin = False
        st.rerun()
