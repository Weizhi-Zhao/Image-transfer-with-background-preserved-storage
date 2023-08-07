# 图片上传和展示项目


这个项目是一个简单的图片上传和展示网页应用，用户可以上传图片并在预览区显示，同时还可以在隐藏菜单中选择不同的风格和迁移方式。
### 2023/8/7 重要描述：1.JavaScript部分获取隐藏菜单选项函数未测试，可能有bug
###                   2.拉取隐藏菜单函数有点小问题，不过不影响使用。
###                   3.选择图片后点击“确定”按钮后需要获取内容传到后端，可以将 -`handleFileUpload(event)` 函数进行如下修改：
```
// 处理图片文件上传事件
function handleFileUpload(event) {
    // 获取上传的图片文件
    const file = event.target.files[0];

    // 显示图片预览
    showSelectedImage(file);

    // 添加“确定”按钮点击事件监听器
    const confirmButton = document.querySelector('.confirm-btn');
    confirmButton.addEventListener('click', function() {
        // 将图片文件传递到后端
        uploadImageToBackend(file);
    });
}

```

## 项目结构

- `new2.html`: 主要的 HTML 文件，包含用户界面和图片上传功能，注意：内嵌Javascript 部分，包含图片预览和隐藏菜单的交互逻辑。
- `styles.css`: CSS 样式文件，用于页面布局和样式定义。

。

## 如何使用

1. 打开页面后，你会看到一个图片上传区域和一个预览区域。
2. 点击“选择文件”按钮，选择一个图片文件，该图片将会在预览区域中显示。
3. 在隐藏菜单中，你可以选择不同的风格和迁移方式。

## JavaScript 函数



在 `scripts.js` 文件中，以下是一些重要的 JavaScript 函数及其功能、输入参数和输出：

- `handleFileUpload(event)`: 处理图片文件上传事件，将上传的图片在预览区显示。
  - 输入：上传的图片文件 (`event.target.files[0]`)。
  - 输出：无。

- `showSelectedImage(file)`: 将选定的图片文件在预览区展示。
  - 输入：选定的图片文件 (`file`)。
  - 输出：无。

- `showMenuDropdownContent()`: 显示隐藏菜单的下拉内容。
  - 输入：无。
  - 输出：无。

- `sendSelectionToBackend(selectedStyle)`: 通过 Ajax 发送用户选择到后台进行记录。
  - 输入：用户选择的风格 (`selectedStyle`)。
  - 输出：无。

## HTML 基本结构

以下是 `index.html` 文件的基本结构：

```html
<!DOCTYPE html>
<html>
<head>
    <title>图片上传和展示</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- 页面主要内容 -->
    <div id="container">
        <!-- ... -->
    </div>

    <!-- 效果图展示区域 -->
    <div id="effect-container">
        <!-- ... -->
    </div>

    <!-- 图片预览区域 -->
    <div id="image-preview">
        <img id="uploaded-image" src="路径/到/默认图片.jpg" alt="上传的图片" />
    </div>

    <!-- 图片上传和确认按钮 -->
    <input type="file" id="upload-input" class="upload-btn" />
    <button class="confirm-btn">确定</button>

    <script src="scripts.js"></script>
</body>
</html>
```
## 注意事项

请确保图片文件的大小适合预览。
如果需要修改页面布局和样式，你可以编辑 styles.css 文件。
如果需要修改交互逻辑，你可以编辑 html类型文件中的script部分。
## 运行端口
默认情况下，项目会在本地运行，端口可能会因你的环境而异。请在浏览器中访问 http://localhost:端口号 来打开页面。

