import React from "react";
import PropTypes from "prop-types";
import {
  Box
} from "@chakra-ui/react";

import { Image } from "@chakra-ui/image"

export default function ImageHero({
  image
}) {
  return (
    <Box w={{ base: "100%"}} mb={{ base: 12, md: 0 }}>
        <Image
        src={image}
        size="100%"
        rounded="md"
        shadow="dark-lg" />
    </Box>
  );
}

ImageHero.propTypes = {
  image: PropTypes.string
};

ImageHero.defaultProps = {
  image: "https://source.unsplash.com/collection/1397626/1200x900",
};