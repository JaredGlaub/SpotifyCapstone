import React from "react";
import Hero from "../components/sections/Hero";
import HeroVideo from "../components/sections/HeroVideo";
import HeroP5 from "../components/sections/HeroP5"
import HeroMLP5 from "../components/sections/HeroMLP5";
import LandingLayout from "../components/layouts/LandingLayout";
import { SimpleGrid } from "@chakra-ui/layout";

export default function Landing() {
  return (
    <SimpleGrid columns = {1} spacing = {10}>
        <LandingLayout>
            <Hero
              title="Welcome to my Final Project"
              subtitle="by Jared Glaub"
              image="dailyMixHeatmap-2.png"
            />
            <HeroVideo
              title="Here's a Training Video"
              subtitle="Where createML StyleTransfer is used on the images above"
              video="https://youtu.be/Lxutpry8xXw"
            />
            <HeroP5
              title="Animation from Augmented Pictures"
              subtitle="Using OpenCV and P5.js for a custom style transfer model"
              video="https://editor.p5js.org/JaredGlaub/full/Y0hZKucLW"
            />
            <HeroMLP5
              title="ML5 can also be used with P5 to embed computer vision"
              subtitle="draw and see!"
              video="https://editor.p5js.org/JaredGlaub/full/K_l_VvmYQ"
            />
        </LandingLayout>
    </SimpleGrid>
  );
}
