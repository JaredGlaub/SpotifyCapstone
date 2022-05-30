import React from "react";
import HeroVideo from "../components/sections/HeroVideo";
import LandingLayout from "../components/layouts/LandingLayout";

export default function Training() {
  return (
    <LandingLayout>
        <HeroVideo
            title="Here's a Training Video"
            subtitle="Where createML StyleTransfer is used on the images above"
            video="https://youtu.be/Lxutpry8xXw"
        />
    </LandingLayout>
  );
}
