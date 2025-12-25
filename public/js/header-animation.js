document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('header');
    if (!header) return;

    // Create container for animation if it doesn't exist
    let animContainer = document.getElementById('header-animation');
    if (!animContainer) {
        animContainer = document.createElement('div');
        animContainer.id = 'header-animation';
        animContainer.style.position = 'absolute';
        animContainer.style.top = '0';
        animContainer.style.left = '0';
        animContainer.style.width = '100%';
        animContainer.style.height = '100%';
        animContainer.style.zIndex = '-1';
        animContainer.style.overflow = 'hidden';

        // Ensure header has relative positioning so absolute child is contained
        const computedStyle = window.getComputedStyle(header);
        if (computedStyle.position === 'static') {
            header.style.position = 'relative';
        }

        header.insertBefore(animContainer, header.firstChild);
    }

    // Create SVG element
    const svgNS = "http://www.w3.org/2000/svg";
    const svg = document.createElementNS(svgNS, "svg");
    svg.setAttribute("width", "100%");
    svg.setAttribute("height", "100%");
    // preserveAspectRatio none allows us to stretch the SVG to fill the container
    svg.setAttribute("preserveAspectRatio", "none");
    animContainer.appendChild(svg);

    // Create Path 1
    const path1 = document.createElementNS(svgNS, "path");
    path1.setAttribute("fill", "rgba(233, 156, 5, 0.05)"); // Very light primary color
    svg.appendChild(path1);

    // Create Path 2
    const path2 = document.createElementNS(svgNS, "path");
    path2.setAttribute("fill", "rgba(233, 156, 5, 0.1)"); // Slightly darker
    svg.appendChild(path2);

    let t = 0;

    function animate() {
        t += 0.005;
        const width = animContainer.clientWidth;
        const height = animContainer.clientHeight;

        // Helper to generate wave path string
        // amplitude, frequency, phase, yOffset
        function getWavePath(amp, freq, phase, yOff) {
            let d = `M0,${amp * Math.sin(phase) + yOff}`;
            for (let x = 0; x <= width; x += 10) {
                const y = amp * Math.sin(freq * x + phase) + yOff;
                d += ` L${x},${y}`;
            }
            d += ` L${width},${height} L0,${height} Z`;
            return d;
        }

        // Animate Path 1
        // Amplitude 30, freq 0.005, phase t, offset 70% down
        const d1 = getWavePath(30, 0.005, t, height * 0.7);
        path1.setAttribute("d", d1);

        // Animate Path 2
        // Amplitude 40, freq 0.008, phase t + 2, offset 80% down
        const d2 = getWavePath(40, 0.008, t + 2, height * 0.8);
        path2.setAttribute("d", d2);

        requestAnimationFrame(animate);
    }

    animate();
});
