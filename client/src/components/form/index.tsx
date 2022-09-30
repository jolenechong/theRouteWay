import Sidebar from '../../components/sidebar';
import { useRef, useState, useMemo } from 'react'

interface IProps {
    source: string,
    destination: string,
}

function Form({ source, destination }: IProps) {
    return (
        <>
            <div className='tw-flex'>
                <form className='tw-pt-0'>
                <h1>One Last Thing! When are you leaving Port {source}?</h1>
                    <div className='tw-flex'>
                    <div>
                    <p className="tw-mt-4">Where are you now?</p>
                    <input
                        type="text"
                        placeholder="Source"
                        value={source}
                        className="tw-mt-2 tw-w-full tw-p-2 tw-border-lightGrey tw-rounded-md focus:tw-border-primary tw-border-2 tw-outline-none"
                    />
                    </div>
                    <div className='tw-ml-2'>
                    <p className="tw-mt-4">Where are you heading?</p>
                    <input
                        type="text"
                        placeholder="Destination"
                        value={destination}
                        className="tw-mt-2 tw-w-full tw-p-2 tw-border-lightGrey tw-rounded-md focus:tw-border-primary tw-border-2 tw-outline-none"
                    />
                    </div>
                    </div>
                    <p className="tw-mt-4">When are you departing?</p>
                    <input
                        type="date"
                        placeholder="Date and Time of Departure"
                        className="tw-mt-2 tw-w-full tw-p-2 tw-border-lightGrey tw-rounded-md focus:tw-border-primary tw-border-2 tw-outline-none"
                    />
                                        <input
                        type="time"
                        placeholder="Date and Time of Departure"
                        className="tw-mt-2 tw-w-full tw-p-2 tw-border-lightGrey tw-rounded-md focus:tw-border-primary tw-border-2 tw-outline-none"
                    />
                    <button className="tw-mt-4 tw-w-full tw-p-2 tw-bg-primary tw-text-white tw-rounded-md hover:tw-bg-primaryDark">Get Route</button>
                </form>
                
            </div>
        </>
    );
}

export default Form;