import React from "react";
import HeroP5 from "../components/sections/HeroP5";
import LandingLayout from "../components/layouts/LandingLayout";

export default function Animated() {
  return (
    <LandingLayout>
        <HeroP5
        title="Animation from Augmented Pictures"
        subtitle="Using OpenCV and P5.js for a custom style transfer model"
        video="https://editor.p5js.org/JaredGlaub/full/Y0hZKucLW"
        />
    </LandingLayout>
  );
}
