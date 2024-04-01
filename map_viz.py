'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    fig.add_trace( go.Choroplethmapbox(
        geojson=montreal_data, 
        locations=locations, 
        featureidkey='properties.NOM',
        z=z_vals,
        colorscale=colorscale, 
        marker_opacity=0.2,
        hovertemplate = hover.map_base_hover_template(),
        showscale=False,
    ))
    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base
    scatter_trace = px.scatter_mapbox(
        street_df,
        lat='LATITUDE',
        lon='LONGITUDE',
        color='TYPE_SITE_INTERVENTION',
        custom_data=['TYPE_SITE_INTERVENTION', 'NOM_PROJET', 'MODE_IMPLANTATION', 'OBJECTIF_THEMATIQUE'],
    )
    scatter_trace.update_traces(marker=dict(size=20))

    for trace in scatter_trace.data:
        
        trace.hovertemplate = hover.map_marker_hover_template(trace.legendgroup)
        
        fig.add_trace(trace)
        
    return fig
