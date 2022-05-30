import React from "react";
import HeroMLP5 from "../components/sections/HeroMLP5";
import LandingLayout from "../components/layouts/LandingLayout";

export default function DoodleNet() {
  return (
    <LandingLayout>
        <HeroMLP5
            title="ML5 can also be used with P5 to embed computer vision"
            subtitle="draw and see!"
            video="https://editor.p5js.org/JaredGlaub/full/K_l_VvmYQ"
        />
    </LandingLayout>
  );
}
