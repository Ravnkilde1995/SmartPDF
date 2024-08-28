    const maxItems = 11;
    let itemCount = 1;

    const itemContainer = document.getElementById('item-container');
    const addItemButton = document.getElementById('add-item');
    const removeItemButton = document.getElementById('remove-item');
    const dateInput = document.getElementById('date');

    const today = new Date().toISOString().split('T')[0];
    dateInput.value = today;

    function addItemField() {
        if (itemCount >= maxItems) {
            alert('Maximum number of items reached');
            return;
        }
        itemCount++;
        const newItemRow = document.createElement('div');
        newItemRow.classList.add('item-row');
        newItemRow.innerHTML = 
            `<label for="item${itemCount}">Product:</label>
            <input type="text" id="item${itemCount}" name="item${itemCount}" maxlength="30">
            <label for="item${itemCount}_qty">Quantity:</label>
            <input type="number" id="item${itemCount}_qty" name="item${itemCount}_qty">`;
        itemContainer.appendChild(newItemRow);
    }

    function removeItemField() {
        if (itemCount <= 1) {
            alert('At least one item must remain');
            return;
        }
        itemCount--;
        itemContainer.removeChild(itemContainer.lastChild);
    }

    addItemButton.addEventListener('click', addItemField);
    removeItemButton.addEventListener('click', removeItemField);