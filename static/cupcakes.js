$(function(){

    updateDom();

    $('#cupcakes-form').on("submit", function(e) {
        e.preventDefault();

        let flavor = $('#flavor').val();
        let size = $('#size').val();
        let rating = $('#rating').val();
        let image = $('#image').val();

        $('#cupcakes-form').trigger("reset");

        addCupcake({flavor, size, rating, image});
        updateDom();
    })

    async function getCupcakes(){
        let response = await axios.get("/api/cupcakes");
        return response.data.cupcakes;
    }

    function addCupcake(cupcakeData){
        axios.post("/api/cupcakes", json = cupcakeData);
    }

    async function updateDom(){
        $('#cupcakes-list').empty();
        let cupcakesList = await getCupcakes();

        for (cupcake of cupcakesList){
            const htmlElement =  
            `<div style="display:inline-block">
                <img src="${cupcake.image}" style="width:200px">
                <div>
                    Flavor: ${cupcake.flavor} <br>
                    Size: ${cupcake.size} <br>
                    Rating: ${cupcake.rating}
                </div>
            </div>`;

            $("#cupcakes-list").append(htmlElement);
        }
    }
})