document.addEventListener('DOMContentLoaded', () => {
    console.log("NailArt.ai - Frontend inicializado.");

    // ==========================================
    // SPARKLE MOUSE EFFECT (Escarcha)
    // ==========================================
    let isMouseMoving = false;
    let sparkleTimeout;

    document.addEventListener('mousemove', (e) => {
        // Limit the rate of sparkle creation to avoid performance issues
        if (Math.random() > 0.3) return; 

        const sparkle = document.createElement('div');
        sparkle.classList.add('sparkle');
        
        // Random size between 2px and 6px
        const size = Math.random() * 4 + 2;
        sparkle.style.width = `${size}px`;
        sparkle.style.height = `${size}px`;
        
        // Position exactly at cursor
        sparkle.style.left = `${e.clientX}px`;
        sparkle.style.top = `${e.clientY}px`;
        
        // Random fall offset
        const fallX = (Math.random() - 0.5) * 50;
        sparkle.style.setProperty('--fall-x', `${fallX}px`);

        document.body.appendChild(sparkle);

        // Remove element after animation completes
        setTimeout(() => {
            if (sparkle.parentNode) {
                sparkle.parentNode.removeChild(sparkle);
            }
        }, 1000);
    });

    // ==========================================
    // DARK MODE LOGIC
    // ==========================================
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const htmlElement = document.documentElement;

    // Check saved theme
    if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        htmlElement.classList.add('dark');
        themeIcon.textContent = '☀️';
    } else {
        htmlElement.classList.remove('dark');
        themeIcon.textContent = '🌙';
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

    // Open/Close Cart
    const toggleCart = () => {
        if (cartModal.classList.contains('hidden')) {
            cartModal.classList.remove('hidden');
            // Small delay to allow display block to apply before animating opacity
            setTimeout(() => {
                cartModal.classList.remove('opacity-0');
                cartDrawer.classList.remove('translate-x-full');
            }, 10);
        } else {
            cartModal.classList.add('opacity-0');
            cartDrawer.classList.add('translate-x-full');
            setTimeout(() => {
                cartModal.classList.add('hidden');
            }, 300); // Wait for transition
        }
    };

    cartBtn.addEventListener('click', toggleCart);
    closeCartBtn.addEventListener('click', toggleCart);
    // Close on click outside
    cartModal.addEventListener('click', (e) => {
        if (e.target === cartModal) toggleCart();
    });

    // Add to Cart
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
            
            // Visual feedback on button
            const originalText = e.target.innerText;
            e.target.innerText = '¡Agregado! 💅';
            e.target.classList.add('bg-pastelPink', 'text-white');
            e.target.classList.remove('text-pastelPink');
            setTimeout(() => {
                e.target.innerText = originalText;
                e.target.classList.remove('bg-pastelPink', 'text-white');
                e.target.classList.add('text-pastelPink');
            }, 1500);
        });
    });

    // Update UI
    const updateCartUI = () => {
        // Update Count
        const totalItems = cart.reduce((sum, item) => sum + item.cantidad, 0);
        cartCount.textContent = totalItems;
        
        // Update Items List
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

            // Add event listeners to remove buttons
            document.querySelectorAll('.remove-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const index = parseInt(e.target.getAttribute('data-index'));
                    cart.splice(index, 1);
                    updateCartUI();
                });
            });
        }

        // Update Total
        const totalAmount = cart.reduce((sum, item) => sum + (item.precio * item.cantidad), 0);
        cartTotal.textContent = `$${totalAmount.toFixed(2)}`;
    };

    // Checkout to WhatsApp
    checkoutBtn.addEventListener('click', () => {
        if (cart.length === 0) {
            alert('Agrega algunos diseños a tu carrito primero 💅');
            return;
        }

        let mensaje = "¡Hola! ✨ Me gustaría pedir el siguiente set de Press-On Nails:%0A%0A";
        
        cart.forEach(item => {
            mensaje += `- ${item.cantidad}x ${item.titulo} ($${(item.precio * item.cantidad).toFixed(2)})%0A`;
        });
        
        const totalAmount = cart.reduce((sum, item) => sum + (item.precio * item.cantidad), 0);
        mensaje += `%0A*Total: $${totalAmount.toFixed(2)}*%0A%0A`;
        mensaje += "¿Podrías indicarme los pasos para el pago y mi medida? Gracias 💖";

        // Reemplaza este número por tu número real de WhatsApp (con código de país, ej: 521XXXXXXXXXX)
        const numeroWhatsApp = "1234567890"; 
        const url = `https://wa.me/${numeroWhatsApp}?text=${mensaje}`;
        
        window.open(url, '_blank');
    });
});
