// // 背景图片列表

// var images = ["../image/background2.jpg", "../image/background1.jpg"];

// var currentIndex = 0;
// var backgroundElement = document.getElementsByTagName("body");

// // 定时切换背景图片
// function changeBackground() {
//   backgroundElement.style.opacity = 0;
//   setTimeout(function () {
//     currentIndex = (currentIndex + 1) % images.length;
//     backgroundElement.style.backgroundImage =
//       "url('" + images[currentIndex] + "')";
//     backgroundElement.style.opacity = 1;
//   }, 1000); // 这里的1000表示淡出淡入的过渡时间，单位为毫秒
// }

// // 初始切换背景图片
// changeBackground();

// // 定时器，每隔一定时间切换背景图片
// setInterval(changeBackground, 5000); // 这里的5000表示切换背景图片的时间间隔，单位为毫秒
