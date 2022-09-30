<template>
    <div class="w-auto h-auto flex justify-center mb-2">
        <div
            class="border-2 border-black rounded-lg overflow-hidden m-5 text-center shadow-[#00000033] ease-in-out duration-300 p-2">
            <div class="flex justify-center">
                <img src=".././assets/star_llena.svg" alt="none" />
            </div>
            <h1 class="text-2xl">titulo</h1>
            <h2 class="text-gray-500 text-lg">autor</h2>
            <h3 class="text-gray-700 text-base mb-6">precio</h3>
            <h3>descripcion</h3>
            <div class="m-6">
                <a class="bg-[#A8D277] p-6 mb-2 font-black cursor-pointer text-center outline-none hover:bg-red-500 active:bg-red-700 py-2 px-8 mt-4 mr-5 border-2 border-solid rounded-lg shadow-lg"
                    href="">
                    Details
                </a>
                <a class="bg-[#A8D277] p-6 mb-2 font-black cursor-pointer text-center outline-none hover:bg-red-500 active:bg-red-700 py-2 px-8 mt-4 mr-5 border-2 border-solid rounded-lg shadow-lg"
                    href="">
                    Cart
                </a>
            </div>
            <h6 class="m-1">5.0</h6>
            <div class=" justify-center grid grid-cols-5 gap-1 ml-20 mr-20">
                <img id="star_1" src=".././assets/star_llena.svg" alt="">
                <img id="star_2" src=".././assets/star_llena.svg" alt="">
                <img id="star_3" src=".././assets/star_llena.svg" alt="">
                <img id="star_4" src=".././assets/star_llena.svg" alt="">
                <img id="star_5" src=".././assets/star_llena.svg" alt="">
            </div>
        </div>
    </div>
</template>