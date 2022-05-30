import React from "react";
import ImageHero from "../components/sections/ImageHero";
import LandingLayout from "../components/layouts/LandingLayout";
import { Box, SimpleGrid } from "@chakra-ui/layout";

export default function SpotifyViz() {

  const outerBoxStyles = {
    boxSize: 'full',
    rounded:"med",
    shadow:"dark-lg",
    p: '10',
    background:
      'black.900',
  }

  return (
    <SimpleGrid columns = {1} spacing = {10}>
      <LandingLayout>
        <Box sx={outerBoxStyles}>
          <SimpleGrid columns = {2} spacing = {2}>
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
            <ImageHero
            image="dailyMixHeatmap-2.png"
            />
            <ImageHero
            image="dailyMixHeatmap-2.png"
            />
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
            <ImageHero
            image="FeatureComparison-3.png"
            />
            <ImageHero
            image="FeatureComparison-3.png"
            />
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
            <ImageHero
            image="DailyMixRecs.png"
            />
            <ImageHero
            image="DailyMixRecs.png"
            />
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
            <ImageHero
            image="MixSamplerCode.png"
            />
            <ImageHero
            image="MixSamplerCode.png"
            />
            <ImageHero
            image="MixSamplerOutput.png"
            />
            <ImageHero
            image="MixSamplerOutput.png"
            />
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
            <ImageHero
            image="https://source.unsplash.com/collection/9037831/1600x150"
            />
          </SimpleGrid>
        </Box>
      </LandingLayout>
    </SimpleGrid>
  );
}
