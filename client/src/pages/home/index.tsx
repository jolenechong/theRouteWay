import Sidebar from '../../components/sidebar';
import { useRef, useState, useMemo } from 'react'
import { Geographies, Geography } from "react-simple-maps"

function Home() {

  // const { isLoaded } = useLoadScript({
  //   googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY ?? "",
  // });

  // if (!isLoaded) return <div>Loading...</div>;

  return (
    <>
    <div className='tw-flex'>
        <Sidebar/>
        <div className='tw-shadow tw-w-[70%] tw-p-4'> 
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15955.418333054597!2d103.82458747671078!3d1.2593576853031703!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31da194fd78713ef%3A0x3a12c6d5a50018b4!2sBrani%20Island!5e0!3m2!1sen!2ssg!4v1664556108637!5m2!1sen!2ssg" width="900" height="580" loading="lazy"></iframe>
        {/* <Map/> */}
        </div>
    </div>
    </>
  );
}

// function Map() {
//   const center = useMemo(() => ({ lat: 44, lng: -80 }), []);

//   return (
//     <GoogleMap zoom={10} center={center} mapContainerClassName="map-container">
//       <Marker position={center} />
//     </GoogleMap>
//   );
// }

export default Home;