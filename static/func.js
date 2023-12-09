document.addEventListener('keyup', function(event) {
    if (event.key === 'ArrowLeft') {
        // 放開左键
        const prevButton = document.querySelector('.previous-button');
        if (prevButton) {
            window.location.href = prevButton.href;  // 导航到上一页
        }
    } else if (event.key === 'ArrowRight') {
        // 放開右键
        const nextButton = document.querySelector('.next-button');
        if (nextButton) {
            window.location.href = nextButton.href;  // 导航到下一页
        }
    }
});

