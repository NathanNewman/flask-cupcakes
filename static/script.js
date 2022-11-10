const BASE_URL = "http://localhost:5000/api";

function generateCupcakeList(cupcake) {
  return `
  <div data-cupcake-id=${cupcake.id}>
    <li>
      ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}/10
      <button class="delete-button">X</button>
    </li>
    <img class="Cupcake-img"
          src="${cupcake.image}"
          alt="(no image provided)">
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

$("#cupcakes-list").on("click", ".delete-button", async function (evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");
  
    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
  });
  
  
  $(showCupcakes);
