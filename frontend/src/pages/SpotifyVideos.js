import React from "react";
import LandingLayout from "../components/layouts/LandingLayout";
import {
    Center,
    Text,
    Heading,
    VStack,
    Button,
    HStack,
    SimpleGrid,
    Box,
    Flex,
    Badge,
    Spinner,
  } from "@chakra-ui/react";

import { useState, useEffect } from "react";


export default function SpotifyVideos() {
    const [isSelected, setIsSelected] = useState(false);
    const [selectedFile, setSelectedFile] = useState(null);
    const [allVideos, setAllVideos] = useState([]);
    const [uploadSuccessful, setUploadSuccessful] = useState(false);
    const [showSpinner, setShowSpinner] = useState(false);

    const outerBoxStyles = {
        boxSize: 'full',
        rounded:"md",
        shadow:"dark-lg",
        p: '10',
        background:
          'black.900',
      }
    
      const innerBoxStyles = {
        rounded:"md",
        shadow:"dark-lg"
      }

    useEffect(() => {
        fetch("http://127.0.0.1:8000/videos")
          .then((response) => response.json())
          .then((data) => {
            setAllVideos(data);
          });
      }, [uploadSuccessful]);
    
      const onInputChange = (e) => {
        console.log(e.target.files[0]);
        setIsSelected(true);
    
        setSelectedFile(e.target.files[0]);
      };
      const onButtonClick = (e) => {
        console.log("Button clicked..");
        e.target.value = "";
      };
    
      const onFileUpload = (e) => {
        setShowSpinner(true);
        const formData = new FormData();
        formData.append("file", selectedFile, selectedFile.name);
        fetch("http://127.0.0.1:8000/videos", {
            method: "POST",
            body: formData,
        })
            .then((response) => response.json())
            .then((data) => {
            console.log("Success posting!!");
            setUploadSuccessful(!uploadSuccessful);
            setShowSpinner(false);
            });
    };

    return (
        <LandingLayout>      
            <Box sx={outerBoxStyles}>
                <Center bg="black" color="white" rounded="md" shadow="dark-lg" padding={8}>
                    <VStack spacing={7}>
                    <Heading>Spotify Video Archive</Heading>
                    <HStack>
                        <input
                        type="file"
                        onChange={onInputChange}
                        onClick={onButtonClick}
                        ></input>

                        <Button
                        size="lg"
                        colorScheme="red"
                        isDisabled={!isSelected}
                        onClick={onFileUpload}
                        >
                        Upload Video
                        </Button>
                        {showSpinner && (
                        <Center>
                            <Spinner
                            thickness='4px'
                            speed='0.65s'
                            emptyColor='gray.200'
                            color='red.800'
                            size='l'
                            />
                        </Center>
                        )}
                    </HStack>
                    <SimpleGrid columns={3} spacing={9}>
                        {allVideos.length !== 0 &&
                        allVideos.map((video) => {
                            return (
                            <Box sx={innerBoxStyles}>
                                <video
                                src={video["video_url"]}
                                controls
                                loop
                                preload="auto"
                                ></video>                  
                                <Flex align="baseline" mt={2}>
                                {/* <Badge variantColor="green">{video["video_url"]}</Badge> */}
                                <Text
                                    ml={2}
                                    textTransform="uppercase"
                                    fontSize="sm"
                                    fontWeight="bold"
                                    color="green.800"
                                >
                                </Text>
                                {/* akdjldsaf */}
                                </Flex>
                            </Box>
                            );
                        })}
                    </SimpleGrid>
                    </VStack>
                </Center>
            </Box>
        </LandingLayout>
    );
}