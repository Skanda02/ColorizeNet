async function upload() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];

  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://localhost:8000/colorize", {
    method: "POST",
    body: formData
  });

  const data = await response.json();
  const hex = data.image;

  const bytes = new Uint8Array(hex.match(/.{1,2}/g).map(b => parseInt(b, 16)));
  const blob = new Blob([bytes], { type: "image/png" });
  document.getElementById("output").src = URL.createObjectURL(blob);
}
