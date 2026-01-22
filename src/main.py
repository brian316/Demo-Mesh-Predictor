from pathlib import Path
from typing import Any, Dict, Optional, Union

from openad_service_utils import (
    DomainSubmodule,
    FileResponse,
    PredictorTypes,
    SimplePredictor
)
from pydantic.v1 import Field
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DemoMeshPredictor(SimplePredictor):
    """
    test mesh predictor
    """

    domain: DomainSubmodule = DomainSubmodule("meshes")
    algorithm_name: str = "Transolver"
    algorithm_application: str = "test"
    algorithm_version: str = "v1"
    property_type: PredictorTypes = PredictorTypes.MESH
    
    # exposed api override parameters
    test_x: Optional[float] = Field(0.0, description="A test float parameter")

    def setup(self):
        logger.info("\nSetting up DemoMeshPredictor...")

    def predict(
        self,
        input: str,
        output_dir: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[FileResponse, Dict[str, Any]]:
        if not output_dir:
            raise ValueError("output_dir must be provided")

        input_path = Path(input)  # input for Mesh type is a filepath
        logger.info("\nRunning prediction in DemoMeshPredictor for input:", input_path.name)
        logger.info("File input path", input_path.absolute().as_posix())
        logger.info("Test parameter test_x:", self.test_x)


        # save input file to output directory as a dummy "prediction"
        output_path = Path(output_dir)
        logger.info("Output directory path:", output_path.absolute().as_posix())
        output_path.mkdir(parents=True, exist_ok=True)
        output_file_path = output_path / f"predicted_{input_path.name}"
        with open(input_path, "rb") as src_file:
            with open(output_file_path, "wb") as dst_file:
                dst_file.write(src_file.read())

        return FileResponse(file_path=output_file_path.as_posix())


# register the predictor
DemoMeshPredictor.register(no_model=True)

if __name__ == "__main__":
    from openad_service_utils import start_server
    start_server(port=8080)
