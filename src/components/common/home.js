import React from 'react'
import axios from 'axios'


class Home extends React.Component{
  constructor(){
    super()

    this.state = {

    }
  }

  getTrips(){
    axios.get('/trips')
      .then(trips => {
        this.setState({results: trips.data})
      })
  }



  render(){
    console.log(this.state)

    return(
      <main>
        <div className="trip-card">
          <div className="contains-title_photo">
            <div className="title">
              <h1> Galle, Sri Lanka </h1>
            </div>
            <div className="showPhotos">
              <img />
              <img />
              <img />
              <img />
            </div>
          </div>

          <div className="contains-budget_duration">
            <div className="budget">
              <h4> £2275 </h4>
            </div>
            <div className="duration">
              <h4> 10 days </h4>
            </div>
          </div>

          <div className="contains-categories">
            <h4>Beach, culture, romantic, food</h4>
          </div>
          <div className="contains-like_viewTrip">
            <h4> 12 likes </h4>
            <button>VIEW</button>
            <i className="far fa-thumbs-up"></i>
          </div>
        </div>
      </div>

      <div className="contains-categories">
        <h4>Beach, culture, romantic, food</h4>
      </div>
      <div className="contains-like_viewTrip">
        <h4> 12 RECS </h4>
        <button>VIEW</button>
        <i className="far fa-thumbs-up"></i>
      </div>
      <div data-skyscanner-widget="SearchWidget"></div>
      <script src="https://widgets.skyscanner.net/widget-server/js/loader.js" async></script>
    </main>

  )
}


export default Home
