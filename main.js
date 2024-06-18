document.addEventListener('DOMContentLoaded', () => {
    const circle = document.getElementById('circle');
    const btn01 = document.getElementById('btn-0.1');
    const btn05 = document.getElementById('btn-0.5');
    const btn1 = document.getElementById('btn-1');
    const slider = document.getElementById('amount-slider');
    const amountLabel = document.getElementById('amount-label');

    circle.addEventListener('click', () => {
        alert('Big blue circle clicked!');
    });

    btn01.addEventListener('click', () => {
        alert('0.1TON button clicked!');
    });

    btn05.addEventListener('click', () => {
        alert('0.5TON button clicked!');
    });

    btn1.addEventListener('click', () => {
        alert('1TON button clicked!');
    });

    slider.addEventListener('input', () => {
        amountLabel.textContent = slider.value;
    });
});
