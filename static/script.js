const BASE_URL = "http://localhost:5000/api";

function generateCupcakeList(cupcake) {
  return `
  <div data-cupcake-id=${cupcake.id}>
    <li>
      <a href="/edit/${cupcake.id}" class="cupcake-text">Flavor: ${cupcake.flavor} | Size: ${cupcake.size} | Rating: ${cupcake.rating}/10</a>
      <button class="delete-button">X</button>
    </li>
    <a href="/edit/${cupcake.id}">
    <img class="cupcake-img"
          src="${cupcake.image}"
          alt="(no image provided)">
    </a>
  </div>
  `;
}

async function showCupcakes() {
  const response = await axios.get(`${BASE_URL}/cupcakes`);

  for (let cupcakeData of response.data.cupcakes) {
    let cupcake = $(generateCupcakeList(cupcakeData));
    $("#cupcake-list").append(cupcake);
  }
}

$("#cupcake-list").on("click", ".delete-button", async function (evt) {
  evt.preventDefault();
  let $cupcake = $(evt.target).closest("div");
  let cupcakeId = $cupcake.attr("data-cupcake-id");

  await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
  $cupcake.remove();
});

$(showCupcakes);
