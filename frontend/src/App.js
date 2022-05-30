import React from "react";
import {Route, Routes} from "react-router-dom";
import { BrowserRouter } from "react-router-dom";

import Landing from "./pages/Landing";
import Animated from "./pages/Animated";
import Training from "./pages/Training";
import DoodleNet from "./pages/DoodleNet";
import SpotifyVideos from "./pages/SpotifyVideos";
import SpotifyViz from "./pages/SpotifyViz";


export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing/>} />
        <Route path='Animated' element={<Animated/>} />
        <Route path='Training' element={<Training/>} />
        <Route path='DoodleNet' element={<DoodleNet/>} />
        <Route path='SpotifyVideos' element={<SpotifyVideos/>} />
        <Route path='SpotifyViz' element={<SpotifyViz/>} />
      </Routes>
    </BrowserRouter>
  );
}
