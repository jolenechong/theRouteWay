import { useNavigate } from "react-router-dom";
import { useState } from "react";

function Sidebar() {

    const [source, setSource] = useState("");
    const [destination, setDestination] = useState("");

    const navigate = useNavigate();
    const handleSubmit = () =>
      navigate({
        pathname: '/route',
        search: `?source=${source}&destination=${destination}`,
      });


  return (
    <>
      <>
        <div className="tw-shadow tw-w-[30%] tw-max-w-[300px] tw-h-screen tw-p-4">
          <h1 className="tw-pt-8">Map View</h1>
          <p>Check Trafic Jam Predictions for roads to avoid.</p>
          <h1 className="tw-pt-8">Get Best Routes</h1>
          <p>Based on our AI Model and Algorithm</p>

          <form>
            <p>Where are you now?</p>
            <input
              type="text"
              placeholder="Source"
              className="tw-mt-2 tw-w-full tw-p-2 tw-border-lightGrey tw-rounded-md focus:tw-border-primary tw-border-2 tw-outline-none"
              onChange={(e) => setSource(e.target.value)}
            />
            <p className="tw-mt-4">Where are you heading?</p>
            <input
              type="text"
              placeholder="Destination"
              className="tw-mt-2 tw-w-full tw-p-2 tw-border-lightGrey tw-rounded-md focus:tw-border-primary tw-border-2 tw-outline-none"
              onChange={(e) => setDestination(e.target.value)}
            />
            <button className="tw-mt-4 tw-w-full tw-p-2 tw-bg-primary tw-text-white tw-rounded-md hover:tw-bg-primaryDark" onClick={handleSubmit}>Get Route</button>
          </form>
        </div>
      </>
    </>
  );
}

export default Sidebar;