// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // --- Form elements ---
  const form = document.querySelector("#contactForm");

  if (!form) {
    console.error("Contact form not found in the HTML!");
    return;
  }

  // --- Modal elements ---
  const modalContainer = document.querySelector("#modal_container");
  const modalMessage = document.querySelector("#modal-message");
  const modalCloseBtn = document.querySelector("#modal-close");

  if (!modalContainer || !modalMessage || !modalCloseBtn) {
    console.error("Modal elements not found in the HTML!");
    return;
  }

  // --- Modal helpers ---
  function openModal(message) {
    modalMessage.textContent = message;
    modalContainer.classList.add("show");
  }

  function closeModal() {
    modalContainer.classList.remove("show");
  }

  // Close when clicking the Close button
  modalCloseBtn.addEventListener("click", closeModal);

  // Optional: close when clicking outside the modal box
  modalContainer.addEventListener("click", (event) => {
    if (event.target === modalContainer) {
      closeModal();
    }
  });

  // --- Form submit handler ---
  form.addEventListener("submit", async (e) => {
    e.preventDefault(); // stop page reload

    // Collect values from the form
    const formData = {
      name: e.target.name.value,
      email: e.target.email.value,
      phone: e.target.phone.value,
      website: e.target.website.value,
      message: e.target.message.value,
    };

    try {
      // Send data to FastAPI backend
      const response = await fetch("https://api.zsolt-csengeri.com/contacts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Server error: " + response.statusText);
      }

      const data = await response.json();

      const name = formData.name.trim();
      const greeting = name ? `Hey ${name}, ` : "Hey, ";

      openModal(
        `${greeting}thanks for contacting me! ✅ Message sent. ID: ${data.id}`
      );

      // Optional: reset the form after success
      form.reset();
    } catch (error) {
      console.error("Error:", error);
      openModal("❌ Failed to send your message. Please try again later.");
    }
  });
});

// Session storage

const $acceptNavigator = document.querySelector(".a-accept");
const $nameFormInput = document.querySelector("#name");
const $emailFormInput = document.querySelector("#email");
const $phoneFormInput = document.querySelector("#phone");
const $websiteFormInput = document.querySelector("#website");
const $messageFormInput = document.querySelector("#message");

$acceptNavigator.addEventListener("click", () => {
  const nameValue = $nameFormInput.value;
  const emailValue = $emailFormInput.value;
  const phoneValue = $phoneFormInput.value;
  const websiteValue = $websiteFormInput.value;
  const messageValue = $messageFormInput.value;

  sessionStorage.setItem("name", nameValue);
  sessionStorage.setItem("email", emailValue);
  sessionStorage.setItem("phone", phoneValue);
  sessionStorage.setItem("website", websiteValue);
  sessionStorage.setItem("message", messageValue);
});

if (sessionStorage.getItem("name")) {
  $nameFormInput.value = sessionStorage.getItem("name");
}
if (sessionStorage.getItem("email")) {
  $emailFormInput.value = sessionStorage.getItem("email");
}
if (sessionStorage.getItem("phone")) {
  $phoneFormInput.value = sessionStorage.getItem("phone");
}
if (sessionStorage.getItem("website")) {
  $websiteFormInput.value = sessionStorage.getItem("website");
}
if (sessionStorage.getItem("message")) {
  $messageFormInput.value = sessionStorage.getItem("message");
}
