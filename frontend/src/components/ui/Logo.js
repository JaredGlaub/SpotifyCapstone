import React from "react";
import { Box, Text } from "@chakra-ui/react";

export default function Logo(props) {
  return (
    <Box {...props}>
      <Text fontSize="medium" fontWeight="bold" className="Menlo">
        Jared Glaub
      </Text>
    </Box>
  );
}