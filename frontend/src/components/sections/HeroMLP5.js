import React from "react";
import PropTypes from "prop-types";
import {
  Box,
  Flex,
  Heading,
  Stack,
  Text
} from "@chakra-ui/react";

export default function HeroMLP5({
  title,
  subtitle,
  video,
  ...rest
}) {
  return (
    <Flex
      align="center"
      justify={{ base: "center", md: "space-around", xl: "space-between" }}
      direction={{ base: "column-reverse", md: "row" }}
      wrap="no-wrap"
      minH="70vh"
      px={8}
      mb={16}
      {...rest}
    >
      <Stack
        spacing={4}
        w={{ base: "80%", md: "40%" }}
        align={["center", "center", "flex-start", "flex-start"]}
      >
        <Heading
          as="h1"
          size="xl"
          fontWeight="bold"
          color="primary.800"
          textAlign={["center", "center", "left", "left"]}
        >
          {title}
        </Heading>
        <Heading
          as="h2"
          size="md"
          color="primary.800"
          opacity="0.8"
          fontWeight="normal"
          lineHeight={1.5}
          textAlign={["center", "center", "left", "left"]}
        >
          {subtitle}
        </Heading>
        <Text
          fontSize="xs"
          mt={2}
          textAlign="center"
          color="primary.800"
          opacity="0.6"
        >
          Created by ML5
        </Text>
      </Stack>
            {/* {video} */}
            <Box w={{ base: "80%", sm: "60%", md: "50%" }} mb={{ base: 12, md: 0 }}> 
                <iframe
                title="training"
                src="https://editor.p5js.org/JaredGlaub/full/K_l_VvmYQ"
                allowFullScreen
                width="600" 
                height="600"
                />
            </Box>
    </Flex>
  );
}

HeroMLP5.propTypes = {
  title: PropTypes.string,
  subtitle: PropTypes.string,
  vid: PropTypes.string,
};

HeroMLP5.defaultProps = {
  title: "React landing page with Chakra UI",
  subtitle:
    "This could be some basic instructions",
  vid: "https://editor.p5js.org/JaredGlaub/full/K_l_VvmYQ"
};