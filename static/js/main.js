document.addEventListener('DOMContentLoaded', () => {
    console.log("Press-On.Nails - Frontend inicializado.");

    // ==========================================
    // SPARKLE MOUSE EFFECT (Escarcha)
    // ==========================================
    document.addEventListener('mousemove', (e) => {
        if (Math.random() > 0.3) return; 

        const sparkle = document.createElement('div');
        sparkle.classList.add('sparkle');
        const size = Math.random() * 4 + 2;
        sparkle.style.width = `${size}px`;
        sparkle.style.height = `${size}px`;
        sparkle.style.left = `${e.clientX}px`;
        sparkle.style.top = `${e.clientY}px`;
        
        const fallX = (Math.random() - 0.5) * 50;
        sparkle.style.setProperty('--fall-x', `${fallX}px`);

        document.body.appendChild(sparkle);
        setTimeout(() => {
            if (sparkle.parentNode) sparkle.parentNode.removeChild(sparkle);
        }, 1000);
    });

    // ==========================================
    // DARK MODE LOGIC
    // ==========================================
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const htmlElement = document.documentElement;

    if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        htmlElement.classList.add('dark');
        themeIcon.textContent = '☀️';
    }

    themeToggleBtn.addEventListener('click', () => {
        htmlElement.classList.toggle('dark');
        if (htmlElement.classList.contains('dark')) {
            localStorage.setItem('theme', 'dark');
            themeIcon.textContent = '☀️';
        } else {
            localStorage.setItem('theme', 'light');
            themeIcon.textContent = '🌙';
        }
    });

    // ==========================================
    // IMAGE VIEWER (LIGHTBOX)
    // ==========================================
    const viewer = document.getElementById('image-viewer');
    const viewerImg = document.getElementById('viewer-img');
    const viewerTitle = document.getElementById('viewer-title');
    const viewerPrice = document.getElementById('viewer-price');
    const closeViewer = document.getElementById('close-viewer');
    const prevBtn = document.getElementById('prev-img');
    const nextBtn = document.getElementById('next-img');
    const catalogContainers = document.querySelectorAll('.catalog-img-container');
    
    let currentIndex = 0;
    const catalogData = [];

    // Recolectar datos del catálogo para el viewer
    catalogContainers.forEach((container, index) => {
        const img = container.querySelector('img');
        const card = container.closest('.group');
        const title = card.querySelector('h3').innerText;
        const price = card.querySelector('.absolute.top-4').innerText;
        
        catalogData.push({
            src: img.src,
            title: title,
            price: price
        });

        container.addEventListener('click', () => {
            openViewer(index);
        });
    });

    const openViewer = (index) => {
        currentIndex = index;
        updateViewer();
        viewer.classList.remove('hidden');
        setTimeout(() => viewer.classList.remove('opacity-0'), 10);
        document.body.style.overflow = 'hidden'; // Bloquear scroll
    };

    const updateViewer = () => {
        const data = catalogData[currentIndex];
        viewerImg.src = data.src;
        viewerTitle.innerText = data.title;
        viewerPrice.innerText = data.price;
    };

    const closeViewerFunc = () => {
        viewer.classList.add('opacity-0');
        setTimeout(() => viewer.classList.add('hidden'), 300);
        document.body.style.overflow = '';
    };

    closeViewer.addEventListener('click', closeViewerFunc);
    viewer.addEventListener('click', (e) => {
        if (e.target === viewer) closeViewerFunc();
    });

    prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + catalogData.length) % catalogData.length;
        updateViewer();
    });

    nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % catalogData.length;
        updateViewer();
    });

    // Soporte para teclado
    document.addEventListener('keydown', (e) => {
        if (viewer.classList.contains('hidden')) return;
        if (e.key === 'Escape') closeViewerFunc();
        if (e.key === 'ArrowLeft') prevBtn.click();
        if (e.key === 'ArrowRight') nextBtn.click();
    });

    // ==========================================
    // SHOPPING CART LOGIC
    // ==========================================
    let cart = [];
    const cartBtn = document.getElementById('cart-btn');
    const cartModal = document.getElementById('cart-modal');
    const cartDrawer = document.getElementById('cart-drawer');
    const closeCartBtn = document.getElementById('close-cart');
    const cartCount = document.getElementById('cart-count');
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    const checkoutBtn = document.getElementById('checkout-whatsapp');
    const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');

    const toggleCart = () => {
        if (cartModal.classList.contains('hidden')) {
            cartModal.classList.remove('hidden');
            setTimeout(() => {
                cartModal.classList.remove('opacity-0');
                cartDrawer.classList.remove('translate-x-full');
            }, 10);
        } else {
            cartModal.classList.add('opacity-0');
            cartDrawer.classList.add('translate-x-full');
            setTimeout(() => cartModal.classList.add('hidden'), 300);
        }
    };

    cartBtn.addEventListener('click', toggleCart);
    closeCartBtn.addEventListener('click', toggleCart);
    cartModal.addEventListener('click', (e) => {
        if (e.target === cartModal) toggleCart();
    });

    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const titulo = e.target.getAttribute('data-titulo');
            const precio = parseFloat(e.target.getAttribute('data-precio'));
            const existingItem = cart.find(item => item.titulo === titulo);
            if (existingItem) {
                existingItem.cantidad += 1;
            } else {
                cart.push({ titulo, precio, cantidad: 1 });
            }
            updateCartUI();
            
            const originalText = e.target.innerText;
            e.target.innerText = '¡Agregado! 💅';
            e.target.classList.add('bg-pastelPink', 'text-white');
            setTimeout(() => {
                e.target.innerText = originalText;
                e.target.classList.remove('bg-pastelPink', 'text-white');
            }, 1500);
        });
    });

    const updateCartUI = () => {
        const totalItems = cart.reduce((sum, item) => sum + item.cantidad, 0);
        cartCount.textContent = totalItems;
        cartItemsContainer.innerHTML = '';
        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<p class="text-gray-400 text-center mt-10 italic">Tu carrito está vacío.</p>';
        } else {
            cart.forEach((item, index) => {
                const itemEl = document.createElement('div');
                itemEl.className = 'flex justify-between items-center bg-white dark:bg-luxuryBlack p-4 rounded-xl border border-gray-100 dark:border-gray-800 transition-colors';
                itemEl.innerHTML = `
                    <div>
                        <h4 class="font-bold text-darkText dark:text-white">${item.titulo}</h4>
                        <p class="text-gray-500 text-sm">$${item.precio.toFixed(2)} x ${item.cantidad}</p>
                    </div>
                    <div class="flex items-center gap-4">
                        <p class="font-bold text-pastelPurple dark:text-luxuryGold">$${(item.precio * item.cantidad).toFixed(2)}</p>
                        <button class="text-red-400 hover:text-red-600 text-xl font-bold remove-btn" data-index="${index}">&times;</button>
                    </div>
                `;
                cartItemsContainer.appendChild(itemEl);
            });
            document.querySelectorAll('.remove-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    cart.splice(parseInt(e.target.getAttribute('data-index')), 1);
                    updateCartUI();
                });
            });
        }
        const totalAmount = cart.reduce((sum, item) => sum + (item.precio * item.cantidad), 0);
        cartTotal.textContent = `$${totalAmount.toFixed(2)}`;
    };

    checkoutBtn.addEventListener('click', () => {
        if (cart.length === 0) { alert('Carrito vacío 💅'); return; }
        let mensaje = "¡Hola! ✨ Me gustaría pedir:%0A%0A";
        cart.forEach(item => mensaje += `- ${item.cantidad}x ${item.titulo} ($${(item.precio * item.cantidad).toFixed(2)})%0A`);
        const totalAmount = cart.reduce((sum, item) => sum + (item.precio * item.cantidad), 0);
        mensaje += `%0A*Total: $${totalAmount.toFixed(2)}*%0A%0A¿Podrías ayudarme con mi pedido?`;
        window.open(`https://wa.me/1234567890?text=${mensaje}`, '_blank');
    });
});
